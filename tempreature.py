import json

# Load the JSON data from the file
with open('weather.json', 'r') as file:
    weather_data = json.load(file)

# Iterate through each temperature entry and print the location and temperature
for entry in weather_data['temperature']['data']:
    location = entry['place']
    temperature = entry['value']
    print(f"Location: {location}, Temperature: {temperature}°C")