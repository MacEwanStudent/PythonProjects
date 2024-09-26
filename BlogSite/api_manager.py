import requests
from dotenv import load_dotenv
import os
class ApiManager:
    def __init__(self, name):
        self.__file_path = os.environ.get("MY_ENV")
        self.__user_agent = os.getenv('USER_AGENT')
        self.__genderize = 'https://api.genderize.io'
        self.__agify = 'https://api.agify.io'
        self.__param = {
            'name': name
        }
        self.header={
            'User-Agent': self.__user_agent,
            'Accept-Language': 'en-US, en;0.5'
        }

        self.__name= name.capitalize()
        self.__gender=''
        self.__age =''
        self.__answer = ''

    def get_data(self, use_genderize=True):
        api_endpoint = self.__genderize if use_genderize else self.__agify

        try:
            # Make the API request
            response = requests.get(url=api_endpoint, params=self.__param, headers=self.header)

            # Check for a successful response (status code 2xx)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()
            print(f"Response {data}")

            return data

        except requests.exceptions.RequestException as e:
            # Handle exceptions such as network issues or invalid responses
            print(f"An error occurred: {e}")
            return None
    def get_result(self):
        self.__gender = self.get_data(True)
        self.__age = self.get_data(False)
        
        self.__answer = f"Hey {self.__name},\n I think you are {self.__gender['gender']}, And maybe {self.__age['age']} years old."
        return self.__answer

