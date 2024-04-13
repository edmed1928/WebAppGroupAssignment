from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City", units="imperial"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units={units}'
    weather_data = requests.get(request_url).json()
    return weather_data
