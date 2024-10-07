import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Documentation at:
# https://platform.openai.com/docs/quickstart?desktop-os=windows&language-preference=python


class OpenAiManager:
    def __init__(self):
        # reads the environment variables
        self.__file_path = os.environ.get("MY_ENV2")
        load_dotenv(dotenv_path=self.__file_path)
        # Once the file is loaded, you can proceed using all the variables inside
        # just as if they were environment variables
        # note: This change is local to the current Python process and its child processes
        #       It will not affect the system-wide environment variables or any other processes.
        self.__API_KEY = os.getenv('OPEN_AI')
        #self.__client = OpenAI(api_key=self.__API_KEY)


# Type of models:
# https://platform.openai.com/docs/models

    def send_message(self, init_model: str = "gpt-4o-mini") -> None:
        completion = self.__client.chat.completions.create(
            model=init_model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a knowledgeable expert in programming and technology."
                               " You provide clear, concise, and accurate insights for technical "
                               "posts tailored for a professional audience."
                }
                ,
                {
                    "role": "user",
                    "content": "Give me three ideas for linkedIn posts"
                }
            ]

        )
        print(completion.choices[0].message)
        return
