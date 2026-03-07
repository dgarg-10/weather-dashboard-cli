import json

FAVORITES_FILE = "favorites_list.json"

def load_favorites():
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_to_favorites(favorites: list, city: str):
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


#Work on adding a display_favorites method
#Work on implementing the functionality within weather.py
