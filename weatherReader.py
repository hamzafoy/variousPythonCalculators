import requests
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

requestedLocation = {
    'city': 'Louisville',
    'latitude': 38.1970,
    'longitude': -85.6633
}

apiKey = os.environ.get('API_KEY')
print(apiKey)
url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(requestedLocation['latitude'])+"&lon="+str(requestedLocation['longitude'])+"&appid="+str(apiKey)

request = requests.get(url)
json = request.json()
print(json['weather'])