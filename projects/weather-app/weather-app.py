import requests
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Use environment variable
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"{data['weather'][0]['description'].title()}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")
    else:
        print("Error:", data.get("message", "Failed to get weather data"))

if __name__ == "__main__":
    city = input("Enter city name: ")
    if not API_KEY:
        print("Error: Please set the OPENWEATHER_API_KEY environment variable.")
    else:
        get_weather(city)