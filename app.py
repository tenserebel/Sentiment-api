from flask import Flask
from flask_cors import *
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import jsonify

sid = SentimentIntensityAnalyzer()
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
def analysis(input1): 
  output=sid.polarity_scores(input1)
  if output['compound']>0:
    return "😁 Positive",output
  elif output['compound']<0:
    return "😭 Negative",output
  else:
    return "😐 Neutral",output

@app.route("/")
@cross_origin()
def homepage():
    return "Api returns sentiment,compound,positive,negative,neutral"
    

@app.route('/<string:sentence>/', methods=['POST','GET'])
@cross_origin() 
def hello(sentence):
    analsed_sentence=analysis(sentence)
    response=jsonify({"sentiment":analsed_sentence[0],"compound":analsed_sentence[1]['compound'],
    "positive":analsed_sentence[1]['pos'],"negative":analsed_sentence[1]['neg'],"neutral":analsed_sentence[1]['neu']})
    return response

if __name__ == '__main__':
    app.run()