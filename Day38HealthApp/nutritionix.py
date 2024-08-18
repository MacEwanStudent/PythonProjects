import json
import requests
import os
IX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
class Nutrionix:
    def __init__(self, query=""):
        self.__query = query
        self.__nutritionix_id = os.environ["APP_ID"]
        self.__ix_key = os.environ["IX_API_KEY"]
        self.__ix_header = {
            "x-app-id": self.__nutritionix_id,
            "x-app-key": self.__ix_key,
            "x-remote-user-id": "0"
        }
        self.__param = {
            "query": self.__query,
            "gender": os.environ["GENDER"],
            "weight_kg": os.environ["WEIGHT"],
            "height_cm": os.environ["HEIGHT"],
            "age": os.environ["AGE"]
        }
        self.__data = None

    def post_request(self):
        self.__param["query"] = self.__query
        response = requests.post(url=IX_URL, json=self.__param, headers=self.__ix_header)
        print(response.text)
        self.__data = response.json()

    def get_data(self):
        return self.__data

    def set_query(self, query):
        self.__query = query
