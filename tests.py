import requests
import json

r = requests.get("https://still-castle-73273.herokuapp.com/getSentiment", params={'number': '1234', 'status': 'sent'})
print(r.text)
