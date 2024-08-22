import os
import requests
from dotenv import load_dotenv

class DataManager:
    def  __init__(self):
        self.__file_path = os.environ.get("MY_ENV")

        load_dotenv(dotenv_path=self.__file_path)
        self.__AUTH_Token = os.getenv('AUTH_TOKEN_SH')
        #self.__url = os.getenv('GSHEET_PATH')
        self.__url= "https://api.sheety.co/b37cf5d1db586a877d54cb4d85c112c7/flightDeals/prices"
        self.__gsheets_header = {
            "Authorization": self.__AUTH_Token
        }
        self.__param = {
            "price": {
                "iataCode": ""
            }
        }
    def get_sheet_info(self):
        print(self.__AUTH_Token)
        response = requests.get(url=self.__url, headers=self.__gsheets_header)
        print(response.json())

    def get_test(self):
        print(self.__AUTH_Token)

    def edit_row(self, obj_id, iata_code):
        url= f"{self.__url}/{(obj_id)}"
        self.__param["price"]["iataCode"]= iata_code
        print(self.__param)
        response = requests.put(url=url, json=self.__param, headers=self.__gsheets_header)
        print(response.status_code)



