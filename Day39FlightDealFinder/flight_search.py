import requests
import os
from dotenv import load_dotenv
class FlightSearch:
    def __init__(self):
        self.__file_path = os.environ.get("MY_ENV")

        load_dotenv(dotenv_path=self.__file_path)
        self.__API_SECRET = os.getenv('API_SECRET')
        self.__API_KEY = os.getenv('API_KEY')
        self.__token = 'tS801YaAR04vwlkg3LBWAniCKUav'

        self.__body= {
            'grant_type': 'client_credentials',
            'client_id': self.__API_KEY,
            'client_secret': self.__API_SECRET
        }

        self.__header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.__auth_header = {
            'Authorization': f"Bearer {self.__token}"
        }


    def get_iata_code(self, city='Tokyo'):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword" : city
        }
        self.__auth_header = {
            'Authorization': f"Bearer {self.__token}"
        }
        response = requests.get(url=url, headers=self.__auth_header, params=params)
        print(response.status_code)
        print(response.json())


    def get_new_token(self):
        print(self.__body)
        url="https://test.api.amadeus.com/v1/security/oauth2/token"
        response = requests.post(url=url, headers=self.__header, data=self.__body)
        print(response.status_code)
        self.__token = response.json()['access_token']
        print("self", self.__auth_header)
        print(self.__token)

