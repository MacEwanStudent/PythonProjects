import json

import requests

class DataManager:
    def __init__(self):
        self.data = []
        self.__end_point = "https://api.npoint.io/674f5423f73deab1e9a7"
        self.__api_call()

    def __api_call(self):
        response = requests.get(self.__end_point)
        self.data= response.json()


    def get_data(self):
        return self.data
