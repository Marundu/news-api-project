import json
import random
import requests

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

api_key='b24ad8f28e1b4e089ee9bca096f11012'

sources=[
'al-jazeera-english', 
'ars-technica', 
'business-insider', 
'buzzfeed', 
'engadget', 
'financial-times', 
'hacker-news', 
'mashable', 
'national-geographic', 
'polygon', 
'recode', 
'reuters', 
'techcrunch', 
'techradar', 
'the-economist', 
'the-guardian-uk', 
'the-next-web', 
'the-new-york-times', 
'the-verge',
'the-huffington-post',
'time',
'the-wall-street-journal',
'the-times-of-india',
'reddit-r-all',
'newsweek',
'new-scientist',
'fortune',
'cnn',
'cnbc',
]

@app.route('/', methods=['GET','POST'])
def articles():
    results=[]
    for source in sources:
        newsapi_url='https://newsapi.org/v1/articles?source={}&sortBy=latest&apiKey='.format(source)
        articles=requests.get(newsapi_url+api_key)
        parsed=articles.json()
        if 'source' in parsed and 'articles' in parsed:
            results.append(parsed)
    return render_template('test_articles.html', parsed=parsed)    


if __name__=='__main__':
    app.run(port=7100, debug=True)
