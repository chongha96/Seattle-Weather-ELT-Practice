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
        response.raise_for_status()
        print("API response successful")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error occured: {e}")

