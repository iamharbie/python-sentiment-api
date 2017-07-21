import os
import re
import sys
import json

import requests
from flask import Flask, request, render_template, jsonify

sys.path.insert(0, "sentiment/sentiment.py")
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

@app.route('/getSentiment', methods=['GET'])
def sentiment():

	# endpoint for processing incoming messaging events

	data = request.get_json()
	data = data.dumps()
	print(data)
	# log(data)
	return jsonify({'message' : 'it works'})


# def log(message):  # simple wrapper for logging to stdout on heroku
# 	print str(message)
# 	sys.stdout.flush()

if __name__ == '__main__':
	app.run(debug=True)