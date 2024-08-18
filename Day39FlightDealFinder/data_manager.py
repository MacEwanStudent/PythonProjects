import os
from dotenv import load_dotenv

class DataManager:

file_path = os.environ.get("MY_ENV")
load_dotenv(dotenv_path=file_path)

MY_ENV_VAR = os.getenv('API_KEY')

print(MY_ENV_VAR)