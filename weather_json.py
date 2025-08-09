import requests

url = 'http://api.weatherapi.com/v1/current.json?key=85e1b077ec0749e28cb120438252207&q=nakuru&aqi=no'

weather_data = requests.get(url)
# Convert the response to JSON format   
weather_json = weather_data.json()

#getting  the city name
City = weather_json.get('location').get('name')

# Extracting the current temperature
temperature = weather_json.get('current').get('temp_c')
Description = weather_json.get('current').get('condition').get('text')
print (f'The current temperature in {City} is {temperature}°C with {Description}.')