import os 
import sys
import requests
import time
from collections import defaultdict
from requests.exceptions import ConnectionError, Timeout, HTTPError




def fetch_current_weather(city: str, api_key: str) -> dict:
    url = "https://api.openweathermap.org/data/2.5/weather"


    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }
    for attempt in range(3):
            try:
                response = requests.get(url, params=params, timeout=10)
                
                if response.status_code == 429:
                    wait_time = 2 ** attempt  # 1s, 2s, 4s
                    print(f"Rate limited. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue  # jump back to the top of the for loop

                response.raise_for_status()
                data = response.json()
                break  # success — exit the retry loop

            except (ConnectionError, Timeout):
                if attempt < 2:  # still have retries left
                    wait_time = 2 ** attempt
                    print(f"Connection issue. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print("Failed after 3 attempts.")
                    return None

            except HTTPError as e:
                if e.response.status_code == 401:
                    print("Invalid API key. Check your WEATHER_API_KEY.")
                elif e.response.status_code == 404:
                    print(f"City not found. Check your spelling.")
                elif e.response.status_code == 429:
                    print("Too many requests. Wait a minute and try again.")
                else:
                    print(f"Server error: {e.response.status_code}")
                return None

            except ValueError:
                print("Received an invalid response from the server.")
                return None



    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    city_name = data["name"]


    # Return a simplified dictionary
  
    return {
        "city": city_name,
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity,
        "description": weather_desc,
        "wind_speed": wind_speed
    }


    


def fetch_five_day_weather(city: str, api_key: str) -> dict:
        url = "https://api.openweathermap.org/data/2.5/forecast"

        params = {
            "q": city,
            "appid": api_key, 
            "units": "imperial"
        } 
        for attempt in range(3):
            try:
                response = requests.get(url, params=params, timeout=10)
                
                if response.status_code == 429:
                    wait_time = 2 ** attempt  # 1s, 2s, 4s
                    print(f"Rate limited. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue  # jump back to the top of the for loop

                response.raise_for_status()
                data = response.json()
                break  # success — exit the retry loop

            except (ConnectionError, Timeout):
                if attempt < 2:  # still have retries left
                    wait_time = 2 ** attempt
                    print(f"Connection issue. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print("Failed after 3 attempts.")
                    return None

            except HTTPError as e:
                if e.response.status_code == 401:
                    print("Invalid API key. Check your WEATHER_API_KEY.")
                elif e.response.status_code == 404:
                    print(f"City not found. Check your spelling.")
                elif e.response.status_code == 429:
                    print("Too many requests. Wait a minute and try again.")
                else:
                    print(f"Server error: {e.response.status_code}")
                return None

            except ValueError:
                print("Received an invalid response from the server.")
                return None

        forecasts = data["list"]
        grouped = defaultdict(list)

        for forecast in forecasts:
            date = forecast["dt_txt"][:10]
            grouped[date].append(forecast)
        
        daily_summaries = []

        for date, forecasts in grouped.items():                
            temps = [e["main"]["temp"] for e in forecasts]

            descriptions = [e["weather"][0]["description"] for e in forecasts]

            summary = {
                "date": date,
                "temp_high": max(temps),
                "temp_low": min(temps),
                "description": max(set(descriptions), key=descriptions.count)
            }
            daily_summaries.append(summary)
        return daily_summaries

