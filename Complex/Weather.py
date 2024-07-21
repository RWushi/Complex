from geopy.geocoders import Nominatim
import requests


def geocode_city(city):
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude) if location else None


def get_weather(coords):
    latitude, longitude = coords
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,relative_humidity_2m,wind_speed_10m'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
