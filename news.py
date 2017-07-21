import json
import requests

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

api_key='b24ad8f28e1b4e089ee9bca096f11012'

aj='al-jazeera-english'
arst='ars-technica'
bi='business-insider'
bf='buzzfeed'
eng='engadget'
ft='financial-times'
hn='hacker-news'
mash='mashable'
natgeo='national-geographic'
pg='polygon'
rc='recode'
rt='reuters'
tc='techcrunch'
tr='techradar'
econ='the-economist'
tguk='the-guardian-uk'
tnw='the-next-web'
nyt='the-new-york-times'
tv='the-verge'

base_url='https://newsapi.org/v1/articles?source={}&sortBy=latest&apiKey='.format(eng)

@app.route('/')
def articles():
	articles=requests.get(base_url+api_key)
	parsed=articles.json()
	
	return render_template('articles.html', source=parsed['source'], articles=parsed['articles'])

if __name__=='__main__':
	app.run(port=7100, debug=True)
