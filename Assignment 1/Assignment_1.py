import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")


def get_weather(city):
    """
    Fetch weather information for a given city using OpenWeatherMap API
    """
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather(weather_data):
    """
    Display current weather, temperature, humidity, and wind speed
    """
    if weather_data:
        print(f"Current weather in {weather_data['name']}:")
        print(f"  Weather: {weather_data['weather'][0]['description']}")
        print(f"  Temperature: {weather_data['main']['temp']}°C")
        print(f"  Humidity: {weather_data['main']['humidity']}%")
        print(f"  Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Error: Unable to fetch weather data")


def main():
    """
    Parse command-line arguments and fetch weather data
    """
    parser = argparse.ArgumentParser(description="Weather CLI Tool")
    parser.add_argument("city", help="City name")
    args = parser.parse_args()
    city = args.city
    weather_data = get_weather(city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()