from dotenv import load_dotenv
import requests
class ApiManager:
    def __init__(self):
        self.__endpoint = 'https://api.npoint.io/71b2059fdb376eeeafd9'
        self.__blogs = []


    def __get_data(self):
        try:
            response = requests.get(url=self.__endpoint)
            self.__blogs = response.json()

        except requests.exceptions.RequestException as e:
        # Handle exceptions such as network issues or invalid responses
            print(f"An error occurred: {e}")
            return None
    def get_blogs(self):
        self.__get_data()
        return self.__blogs

    def get_blog(self, id):
        for blog in self.__blogs:
            if int(blog['id']) == int(id):
                return blog

        return None