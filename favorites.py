import json
from api import fetch_current_weather
from weather import display_weather

FAVORITES_FILE = "favorites_list.json"

def load_favorites():
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def add_to_favorites(favorites: list, city: str):
    city = city.lower()

    if city in favorites:
        print(f"{city.capitalize()} is already in your favorites.")
    else:
        favorites.append(city)
        with open(FAVORITES_FILE, "w") as f:
            json.dump(favorites, f)
    
def remove_from_favorites(favorites: list, city: str):
    city = city.lower()

    if city not in favorites:
        print(f"{city.capitalize()} is not in your favorites.")
    else:
        favorites.remove(city)
        with open(FAVORITES_FILE, "w") as f:
            json.dump(favorites, f)

def display_favorites(favorites: list, api_key):
    if not favorites:
        print("No favorites have been saved.")
    else:
        for city in favorites:
            weather = fetch_current_weather(city, api_key)
            if weather is not None:              
                display_weather(weather)



