from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


app = Flask(__name__, static_url_path='/static')

app.secret_key = "nothing"

nltk.download('stopwords')

set(stopwords.words('english'))
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

@app.route('/', methods=['POST'])
def post():
    stop_words = stopwords.words()
    text = request.form['text'].lower()

    doc = ' '.join([word for word in text.split() if word not in stop_words])

    sent_analysis = SentimentIntensityAnalyzer()
    pol = sent_analysis.polarity_scores(text=doc)
    compound = round((1 + pol['compound'])/2, 2)

    return render_template('home.html', final=compound, text=text)

if __name__ == "__main__":
	app.run(port=5000, debug=True, threaded=True)