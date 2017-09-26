import json
import random
import requests

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

api_key='b24ad8f28e1b4e089ee9bca096f11012'

sources_list=[
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
    'the-verge'
    ]

for i in range(len(sources_list)):
    random_sources_list=random.shuffle(sources_list)
    source=random.choice(sources_list)

base_url='https://newsapi.org/v1/articles?source={}&sortBy=latest&apiKey='.format(source)

@app.route('/')
def articles():
    articles=requests.get(base_url+api_key)
    parsed=articles.json()
    try:
        source=parsed['source']
        articles=parsed['articles']
        return render_template('articles.html', source=source, articles=articles)

    except KeyError:
        return render_template('error.html')

if __name__=='__main__':
    app.run(port=7100, debug=True)
