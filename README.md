# Interactive Weather CLI

A Python command-line tool for looking up current weather conditions and forecasts by city.


## Example Usage

```
=============================================
  Current Weather for Seattle
=============================================
  Temperature:   55.9°F
  Feels Like:    54.4°F
  Humidity:      68%
  Wind Speed:    6.91 mph
  Conditions:    Overcast Clouds
=============================================

  Date           High       Low        Conditions
  --------------------------------------------------
  04/29/2026     64.7°F     46.2°F     Overcast Clouds
  04/30/2026     69.2°F     47.0°F     Clear Sky
  05/01/2026     68.5°F     47.9°F     Overcast Clouds
  05/02/2026     67.0°F     46.4°F     Overcast Clouds
  05/03/2026     77.2°F     53.2°F     Scattered Clouds
```

## Tech Stack

Python 3.12
I used the OpenWeatherMap API because it is open-source and easy to implement.

## Running Locally

```bash
git clone https://github.com/dgarg-10/weather-dashboard-cli.git
cd weather-dashboard-cli
pip install -r requirements.txt
python weather.py [city_name]
```

You will need an OpenWeatherMap API Key. You can get a free one by signing up on their website openweathermap.org and creating your own API key. 
From there, you can save it as an environment variable in your .env file as WEATHER_API_KEY=your_key, to access it in the future.

## What I Learned

From this project, I learned how to deal with handling API errors with grace by printing out a message to indicate that an error has occured. 
I was also able to learn about how to use caching in order to avoid unneccessary fetch calls towards the API by storing recently used cities 
in the cache, so that the user can access them faster if they want the information again. 

