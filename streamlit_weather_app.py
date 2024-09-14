import streamlit as st
import json
import pandas as pd

import requests
import json

# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# Save the JSON response to a file
with open('weather.json', 'w') as f:
 output_json = json.dumps(result.json(), indent=4, sort_keys=True)
 f.write(output_json)

# Load the JSON data from the file
with open('weather.json', 'r') as file:
    weather_data = json.load(file)

# Extract locations and temperatures
locations = [entry['place'] for entry in weather_data['temperature']['data']]
temperatures = [entry['value'] for entry in weather_data['temperature']['data']]

# Create a DataFrame for the bar chart
df = pd.DataFrame({
    'Location': locations,
    'Temperature': temperatures
})

# Streamlit app
st.title("Weather Data")

# Sidebar for selecting a location
selected_location = st.sidebar.selectbox("Select a location", locations)

# Display bar chart of temperatures
st.write("### Temperature of all locations")
st.bar_chart(df.set_index('Location'))

# Display temperature for the selected location
selected_temp = df[df['Location'] == selected_location]['Temperature'].values[0]
st.write(f"### Temperature at {selected_location}: {selected_temp}°C")