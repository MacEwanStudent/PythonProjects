from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

ITEM_URL="https://www.amazon.ca/Tassimo-Nabob-Espresso-Single-T-Discs/dp/B06X93NNZ7?th=1"

# To get your user-agent follow the following link
# https://www.whatismybrowser.com/detect/what-is-my-user-agent/

class AmazonItemScraper:
    def __init__(self, url=ITEM_URL):
        self.__file_path = os.environ.get("MY_ENV")
        self.__user_agent = os.getenv('USER_AGENT')
        self.__url = url
        self.__price = None
        self.__get_price_info()

    def __get_price_info(self):
        Headers = (
            {
                'User-Agent': self.__user_agent,
                'Accept-Language': 'en-US, en;0.5'
            }
        )
        response = requests.get(self.__url, headers=Headers)
        print("Status code",response.status_code)
        amazon_web_page = response.text

        soup = BeautifulSoup(amazon_web_page, "html.parser")
        price_info = soup.find(
            name="div",
            attrs={
                "id": "corePriceDisplay_desktop_feature_div",
                "class": "celwidget",
                "data-feature-name": "corePriceDisplay_desktop",
                "data-csa-c-type": "widget"
                # "data-csa-c-content-id": "corePriceDisplay_desktop",
                # "data-csa-c-slot-id": "corePriceDisplay_desktop_feature_div",
                # "data-csa-c-asin": "B06X93NNZ7"
                # "data-csa-c-is-in-initial-active-row": "false",
                # "data-csa-c-id": "4wg2ip-7yl8ll-mvlirk-uqxb29",

            }
        ).find(
            name='span',
            class_='aok-offscreen'
        ).text
        print("PRICE INFo", price_info)
        price_info = price_info.lstrip()
        self.__price = price_info.split(' ')[0]
        self.__price = float(self.__price[1:])

        print("Converted price to float", self.__price)
        print("Items")

    def get_price(self):
        return self.__price
