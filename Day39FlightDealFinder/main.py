from data_manager import DataManager
import pandas as pd
from flight_search import FlightSearch
from dotenv import load_dotenv
import os
flight_manager=FlightSearch()
new_info= DataManager()

data = {'prices': [{'city': 'Vienna', 'iataCode': '', 'economyLowestPrice': 600, 'businessLowestPrice': 1800, 'id': 2}, {'city': 'Bangkok', 'iataCode': '', 'economyLowestPrice': 600, 'businessLowestPrice': 1800, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'economyLowestPrice': 600, 'businessLowestPrice': 1800, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'economyLowestPrice': 600, 'businessLowestPrice': 1800, 'id': 5}, {'city': 'Ho Chi Minh City', 'iataCode': '', 'economyLowestPrice': 600, 'businessLowestPrice': 1800, 'id': 6}, {'city': 'Mexico City', 'iataCode': '', 'economyLowestPrice': 400, 'businessLowestPrice': 1000, 'id': 7}]}
sheet_data= data['prices']
df = pd.DataFrame(sheet_data)

# Print the DataFrame in a table format
print(df)
def check_codes():
    for item in sheet_data:
        if item['iataCode'] == '':
            flight_manager.get_iata_code()

#check_codes()
# update IATA code for empty fields
#new_info.edit_row(2,"Testing")

flight_manager.get_new_token()
flight_manager.get_iata_code()

#
# new_info.get_test()
# new_info.get_sheet_info()
