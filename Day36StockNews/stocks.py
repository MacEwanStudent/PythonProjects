import requests
from mylib.myinfo import MyInfo
import yaml
class StockInfo:
    def __init__(self, function, symbol):
        self.__url = "https://www.alphavantage.co/query"
        self.__keys = MyInfo()
        self.__params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.__keys.get_info("Alphavantage", "STOCK_API_KEY")
        }
        self.__data = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2024-08-01', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2024-08-01': {'1. open': '227.6900', '2. high': '231.8670', '3. low': '214.3328', '4. close': '216.8600', '5. volume': '82881451'}, '2024-07-31': {'1. open': '227.9000', '2. high': '234.6800', '3. low': '226.7875', '4. close': '232.0700', '5. volume': '67497011'}, '2024-07-30': {'1. open': '232.2500', '2. high': '232.4100', '3. low': '220.0000', '4. close': '222.6200', '5. volume': '100560334'}, '2024-07-29': {'1. open': '224.9000', '2. high': '234.2700', '3. low': '224.7000', '4. close': '232.1000', '5. volume': '129201789'}}}


    def get_time_series(self):
        response = requests.get(self.__url, self.__params)
        self.__data = response.json()

        print("Data obtained!")
    def get_close(self, day):
        return self.__data["Time Series (Daily)"][day]["4. close"]

    def get_data(self):
        return self.__data
