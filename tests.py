import requests
import json

r = requests.get("https://still-castle-73273.herokuapp.com/getSentiment", params={'keyword': 'tesla'})
print(r.text)
