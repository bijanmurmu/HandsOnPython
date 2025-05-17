# Simple Python Weather App

A simple command-line weather app using the OpenWeatherMap API.

## Features
- Current temperature, humidity, wind speed, and description.
- Uses metric units (Celsius, m/s).

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/bijanmurmu/HandsOnPython.git
   cd HandsOnPython/weather-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   python weather-app.py
   ```

## Example Output

```
Enter city name: kolkata
Weather in Kolkata, IN:
Clear Sky
Temperature: 28.97°C
Humidity: 80%
Wind: 3.06 m/s
```