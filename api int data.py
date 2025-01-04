import requests
import matplotlib.pyplot as plt
from datetime import datetime
import json

# Constants
API_KEY = '315a2ee51537fbd09f26c864221eb36c'  #  OpenWeatherMap API key
CITY = 'India'
API_URL = 'https://api.openweathermap.org/data/2.5/forecast'

# Function to get weather data
def get_weather_data(city, api_key):
    # Request parameters
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use 'metric' for Celsius or 'imperial' for Fahrenheit
        'cnt': 40  # Number of data points (forecast data for 5 days, 3-hour intervals)
    }
    try:
        # Make API request
        response = requests.get(API_URL, params=params)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to extract relevant data from the API response
def extract_data(weather_data):
    timestamps = []
    temperatures = []

    # Parse the JSON response and extract timestamps and temperatures
    for entry in weather_data['list']:
        timestamps.append(datetime.utcfromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
    
    return timestamps, temperatures

# Function to visualize the weather data using Matplotlib
def visualize_weather_data(timestamps, temperatures):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label='Temperature (°C)', color='blue', marker='o')
    
    plt.title(f"Temperature Forecast for {CITY}", fontsize=16)
    plt.xlabel('Timestamp', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    plt.xticks(rotation=45)  # Rotate timestamps for better readability
    plt.grid(True)
    plt.tight_layout()
    
    plt.legend()
    plt.show()

# Main function to integrate all steps
def main():
    # Get weather data from the API
    weather_data = get_weather_data(CITY, API_KEY)
    
    if weather_data:
        # Extract data from the API response
        timestamps, temperatures = extract_data(weather_data)
        
        # Visualize the extracted data
        visualize_weather_data(timestamps, temperatures)

if __name__ == '__main__':
    main()
