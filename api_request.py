import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Seattle"

#Function to send a request to weatherstack API
def fetch_data():
    try:
        #Requesting data from weatherstack
        response = requests.get(api_url)
        # If the response was successful (e.g., 200 OK), no exception is raised
        # If the response is a client or server error (e.g., 404 Not Found, 500 Internal Server Error), 
        # an HTTPError is raised
        response.raise_for_status()
        print("API response successful")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occured: {e}")


"""
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-03-07 23:25', 'localtime_epoch': 1772925900, 'utc_offset': '-5.0'}, 'current': {'observation_time': '04:25 AM', 'temperature': 10, 'weather_code': 143, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0006_mist.png'], 'weather_descriptions': ['Mist'], 'astro': {'sunrise': '06:20 AM', 'sunset': '05:54 PM', 'moonrise': '10:38 PM', 'moonset': '07:56 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 87}, 'air_quality': {'co': '146.85', 'no2': '21.65', 'o3': '38', 'so2': '7.25', 'pm2_5': '12.15', 'pm10': '12.25', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 10, 'wind_degree': 190, 'wind_dir': 'S', 'pressure': 1013, 'precip': 0, 'humidity': 96, 'cloudcover': 100, 'feelslike': 9, 'uv_index': 0, 'visibility': 8, 'is_day': 'no'}}
    """