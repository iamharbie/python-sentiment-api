import requests
import json
import re

r = requests.get("https://still-castle-73273.herokuapp.com/getSentiment", params={'keyword': 'Piers_Morgan'})
print(r.text)


