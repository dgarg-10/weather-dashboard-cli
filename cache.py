import json
import time

CACHE_FILE = "weather_cache.json"

def load_cache():
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_cache(cache, city, weather_data, forecast_data):
    cache[city.lower()] = {
        "weather": weather_data,
        "forecast": forecast_data,
        "time": time.time()
    }
    
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)
    
def get_cached_data(city, cache, max_age=600):
    city = city.lower()

    if city not in cache:
        return None

    entry = cache[city]
    age = time.time() - entry["time"]

    if age > max_age:
        return None
    return entry