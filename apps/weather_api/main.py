import requests
import datetime

print('Wpisz miasto')
city = input('>')
print('Wpisz kod pocztowy')
postal_code = input('>')
key = 'INSERT GEOCODE KEY HERE'

url_geocode = f'http://www.mapquestapi.com/geocoding/v1/address?key={key}&location={postal_code},{city}'
response_geocode = requests.get(url_geocode)
geocode = response_geocode.json()
lat = geocode['results'][0]['locations'][0]['latLng']['lat']
long = geocode['results'][0]['locations'][0]['latLng']['lng']


url_weather = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}' \
              f'&hourly=temperature_2m,pressure_msl,cloudcover'
response_weather = requests.get(url_weather)
weather = response_weather.json()
now = datetime.datetime.now()
current_time = now.hour
current_temp = weather['hourly']['temperature_2m'][current_time]
current_press = weather['hourly']['pressure_msl'][current_time]
current_cloud = weather['hourly']['cloudcover'][current_time]

print(f'Temperatura: {current_temp} Celcjusza, ciśnienie: {current_press} hPa, Procent zachmurzenia: {current_cloud} %')
