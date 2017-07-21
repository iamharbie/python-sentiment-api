import os
import re
import sys
import json

import requests
from flask import Flask, request, render_template, jsonify

import sentiment as se

app = Flask(__name__)

# this is the index get method that displays a template that shows at the main heroku webpage
@app.route('/', methods=['GET'])
def root():
	return render_template('index.html')

# no POST methods in this application
@app.route('/', methods=['POST'])
def webhook():
	return "ok", 200

# this is the main GET method for this application
# when an application wants to use this API they need to call a GET request on /getSentiment
@app.route('/getSentiment', methods=['GET'])
def sentiment():
	try:
		keyword = request.args.get('keyword')
		ret_dict = se.sentimentSearchAnalysis(keyword)
		return jsonify({'Return Dictionary' : ret_dict})
	except:
		return jsonift({'empty': 'null'})



# def log(message):  # simple wrapper for logging to stdout on heroku
# 	print str(message)
# 	sys.stdout.flush()

if __name__ == '__main__':
	app.run(debug=True)