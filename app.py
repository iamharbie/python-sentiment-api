import os
import re
import sys
import json

import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def webhook():

	# endpoint for processing incoming messaging events

	data = request.get_json()
	# log(data)
	message_to_send = data['number']
	return "ok", 200

@app.route('/getSentiment', methods=['GET'])
def sentiment():

	# endpoint for processing incoming messaging events

	data = request.get_json()
	# log(data)
	return jsonify({'message' : 'it works'})


# def log(message):  # simple wrapper for logging to stdout on heroku
# 	print str(message)
# 	sys.stdout.flush()

if __name__ == '__main__':
	app.run(debug=True)