import requests
import json

r = requests.get("https://still-castle-73273.herokuapp.com/getSentiment", params={'keyword': 'apple'})
print(r.text)
