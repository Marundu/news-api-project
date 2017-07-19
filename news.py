import json
import requests

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

api_key='&apiKey=b24ad8f28e1b4e089ee9bca096f11012'
base_url='https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest'

@app.route('/')
def articles():
	articles=requests.get(base_url+api_key)
	parsed=articles.json()
	source=parsed['source']
	title=parsed['articles'][0]['title']
	description=parsed['articles'][0]['description']
	url=parsed['articles'][0]['url']
	
	return render_template('articles.html',
			source=source, 
			title=title, 
			description=description, 
			url=url
			)

if __name__=='__main__':
	app.run(port=7100, debug=True)
