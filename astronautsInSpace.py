from itertools import count
import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
countOfAstronauts = len(json['people'])

for x in range(countOfAstronauts):
    print(json['people'][x]['name'])
