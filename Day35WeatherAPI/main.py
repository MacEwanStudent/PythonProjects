import requests
from twilio_msg import SendMsg
import os
from mylib.myinfo import MyInfo
import yaml

URL = "https://api.openweathermap.org/data/2.5/forecast"
UMBRELLA = "☔"

# Using Environment Variable for security purposes
my_info = MyInfo()
MY_API = my_info.get_info("OpenWeatherKey","OWN_API_KEY")
my_msg = SendMsg()

open_weather = {
    "lat": 53.631611,
    "lon": -113.323975,
    "appid": MY_API,
    "cnt": 4,
    "units": "metric"
}


def send_request(url: str, parameters: dict):
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    api_dict = response.json()["list"]
    forecast_data = [int(temp["weather"][0]["id"] // 100) for temp in api_dict]
    print("fore", forecast_data)
    return forecast_data


def check_rain(forecast_data):
    rain = False
    for code in forecast_data:
        if code < 8:
            rain = True
            break

    return rain


def check_rain_status():
    if check_rain(send_request(URL, open_weather)):
        msg = f"It will rain {UMBRELLA}"
        my_msg.set_message(msg)
        my_msg.send_whatsapp()


check_rain_status()

