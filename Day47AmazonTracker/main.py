from amazon import AmazonItemScraper
from mail import SendEmail
from datetime import datetime
from savetofile import DataManager

IDEAL_VALUE = 28.00
coffee_info = AmazonItemScraper()
price= coffee_info.get_price()
def check_price(price):
    if price < IDEAL_VALUE:
        pass # Send mail

def append_to_file(price=41.21):
    date_obj = datetime.today().strftime('%Y-%m-%d')

    my_test = DataManager(date_obj, price)

    print(date_obj, price)

append_to_file(price)


send_mail=SendEmail(body=price)
send_mail.send_message()