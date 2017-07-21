# Python Sentiment API

* This is a backend for an iOS app in the works written in Python and hosted on Heroku
* The python handles the HTTP GET Request set by the iOS app and returns a dictionary of results
* The GET function from inside app.py calls a method from within sentiments.py
* Sentiments.py runs a sentiment analysis on the last 100 tweets using the keyword provided by the user on the client-side
* It then returns to the client, how many of the tweets were positive, neutral, or negative

* This application can be used to gauge puplic opinion on keywords/companies/ideas in order to predict financial futures
