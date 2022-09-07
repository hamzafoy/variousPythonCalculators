import requests
import os
import dotenv
import json
from dotenv import load_dotenv
load_dotenv()

# currencies = {
#     'England': 'GBP',
#     'Europe': 'EUR',
#     'Iraq': 'IQD',
#     'Japan': 'JPY',
#     'United Arab Emirates': 'AED'
# }

apiKey = os.environ.get('CURRENCY_API_KEY')
url = "https://openexchangerates.org/api/latest.json?app_id="+str(apiKey)
request = requests.get(url)
json = request.json()
print(json['rates'])

def exchange_currency(amount, currencyabbrev):
    print(json['rates'][currencyabbrev])
    expectedExchange = (amount * json['rates'][currencyabbrev])
    return expectedExchange

print(exchange_currency(10, 'JPY'))