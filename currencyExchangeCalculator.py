import requests
import os
import dotenv
import json
from dotenv import load_dotenv
load_dotenv()

apiKey = os.environ.get('CURRENCY_API_KEY')
url = "https://openexchangerates.org/api/latest.json?app_id="+str(apiKey)

request = requests.get(url)
json = request.json()
print(json['rates'])