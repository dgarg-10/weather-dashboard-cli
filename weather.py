import sys
import os
from api import fetch_current_weather, fetch_five_day_weather
from cache import load_cache, get_cached_data, save_cache

def display_weather(weather):
    print()
    print("=" * 45)
    print(f"  Current Weather for {weather['city']}")
    print("=" * 45)
    print(f"  Temperature:   {weather['temp']:.1f}°F")
    print(f"  Feels Like:    {weather['feels_like']:.1f}°F")
    print(f"  Humidity:      {weather['humidity']}%")
    print(f"  Wind Speed:    {weather['wind_speed']} mph")
    print(f"  Conditions:    {weather['description'].title()}")
    print("=" * 45)


def display_forecast(daily_summaries):
    print()
    print(f"  {'Date':<14} {'High':<10} {'Low':<10} {'Conditions'}")
    print(f"  {'-' * 50}")

    for day in daily_summaries:
        raw_date = day["date"]
        date = raw_date[5:7] + "/" + raw_date[8:] + "/" + raw_date[:4]
        high = f"{day['temp_high']:.1f}°F"
        low = f"{day['temp_low']:.1f}°F"
        desc = day["description"].title()
        print(f"  {date:<14} {high:<10} {low:<10} {desc}")

api_key = os.environ.get("WEATHER_API_KEY")

if api_key is None:
    print("Error: Please set your WEATHER_API_KEY. ")
    sys.exit(1)

if len(sys.argv) > 1:
    city = ' '.join(sys.argv[1::])
else:
    city = input("Enter a city name please: ").strip()

if not city:
    print("Please provide a city name.")
    sys.exit(1)



cache = load_cache()

cached_entry = get_cached_data(city, cache)

if cached_entry is not None:
    weather = cached_entry["weather"]
    forecast = cached_entry["forecast"]
    print("Cached Data")
else:
    weather = fetch_current_weather(city, api_key)
    forecast = fetch_five_day_weather(city, api_key)
    if weather is not None and forecast is not None:
        save_cache(cache, city, weather, forecast)
    
if weather is not None:
    display_weather(weather)
if forecast is not None:
    display_forecast(forecast)



