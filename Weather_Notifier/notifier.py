"""
Weather Notifier Script
-----------------------
Fetches live weather updates for a specified city using the OpenWeather API.

Created on: Sep 2, 2025
Author: Vineet Gawali
"""

import sys
import requests

# NOTE: This API key was found publicly online and is used here for demonstration purposes only.
# It may be revoked at any time or have usage limits.
# Please obtain your own API key from https://openweathermap.org/api for personal or production use.
# Do NOT misuse this key or share it inappropriately to avoid service disruption or violation of terms.
API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # Don't be surprised, I found this API key online. This is not my API key

def get_weather(city: str):
    """
    Fetch weather data for the given city from OpenWeather API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return

    data = response.json()

    # Check if city was found
    if data.get("cod") != 200:
        print(f"❌ City not found: {city}")
        return

    # Extract weather details
    name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"].capitalize()

    # Print formatted weather info
    print(f"🌤 Weather in {name}, {country}")
    print("-" * 30)
    print(f"Temperature     : {temp}°C")
    print(f"Feels Like      : {feels_like}°C")
    print(f"Condition       : {description}")
    print(f"Humidity        : {humidity}%")
    print(f"Wind Speed      : {wind_speed} m/s")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        city_name = sys.argv[1]
    else:
        city_name = input("🏙️ Enter the city name: ").strip()

    get_weather(city_name)
