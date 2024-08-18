import os
import json
import requests

class GSheets:
    def __init__(self):
        self.__gsheets_auth = os.environ["AUTH_TOKEN"]
        self.__gsheets_header = {
            "Authorization": self.__gsheets_auth
        }
        self.__param = {
            "workout" : {
                "date": "",
                "time": "",
                "exercise" : "",
                "duration" : "",
                "calories" : ""
            }
        }
        self.__url = os.environ["GSHEET_URL"]
        self.__data = None

    def update_sheet(self):
        response = requests.post(url=self.__url, json=self.__param, headers=self.__gsheets_header)
        print(response.status_code)

    def set_row(self, row):
        self.__param = {
            "workout": {
                "date": row[0],
                "time": row[1],
                "exercise": row[2],
                "duration": row[3],
                "calories": row[4]
            }
        }