import os
import requests
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
NOAA_API_KEY = os.getenv("NOAA_API_KEY")

def fetch_nasa_data():
    url = f"https://api.nasa.gov/planetary/some-endpoint?api_key={NASA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/raw/nasa_data.json', 'w') as file:
            file.write(response.text)
        print("NASA data fetched successfully.")
    else:
        print(f"Failed to fetch NASA data: {response.status_code}")

def fetch_noaa_data():
    url = f"https://www.noaa.gov/weather-api/some-endpoint?api_key={NOAA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/raw/noaa_data.json', 'w') as file:
            file.write(response.text)
        print("NOAA data fetched successfully.")
    else:
        print(f"Failed to fetch NOAA data: {response.status_code}")

if __name__ == "__main__":
    fetch_nasa_data()
    fetch_noaa_data()
