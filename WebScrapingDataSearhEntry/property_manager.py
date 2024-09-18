from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import time

# Use the following command to install the dotenv library:
# pip install python-dotenv
class PropertyManager():
    def __init__(self):
        self.__file_path = os.environ.get("MY_ENV")
        load_dotenv(dotenv_path=self.__file_path)
        self.__gsheet_url=os.getenv('GOOGLE_QUESTIONS')
        self.__properties=[]
        #self.__real_sate_endpoint = "https://realestate.co.jp/en/forsale/listing?prefecture=JP-13&city=&trainline=11302&station=1130203&min_cap_rate=&min_price=&max_price=&min_meter=&rooms=&distance_station=&agent_id=&building_type=mansion-apartment&building_age=&updated_within=&transaction_type=&occupancy=&order=&search=Search&page=1"
        #self.__real_sate_endpoint = "https://realestate.co.jp/en/forsale/listing?prefecture=JP-13&city=&trainline=11302&station=1130201&min_cap_rate=&min_price=&max_price=&min_meter=&rooms=&distance_station=&agent_id=&building_type=mansion-apartment&building_age=&updated_within=&transaction_type=&occupancy=&order=&search=Search&page=1"
        #self.__real_sate_endpoint = 'https://realestate.co.jp/en/forsale/listing?prefecture=JP-13&city=&trainline=11302&station=1130203&max_price=&search=Search&page=1'
        self.__real_sate_endpoint= 'https://realestate.co.jp/en/forsale/listing?prefecture=JP-13&city=&trainline=11302&station=1130219&min_cap_rate=&min_price=&max_price=&min_meter=&rooms=&distance_station=&agent_id=&building_type=mansion-apartment&building_age=&updated_within=&transaction_type=&occupancy=&order=&search=Search'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.__driver= webdriver.Chrome(options=chrome_options)
        self.__driver.get(self.__real_sate_endpoint)
        self.__property_data = {
            'Location': "",
            'Price': 0.0,
            'Size': "",
            'Floor': "",
            'Year Built': 0,
            'Link': "",
            'Distance': "",
            'Image': ""
        }


    def get_data(self):

        next_page = True
        while next_page:
            raw_data = self.__driver.find_elements(By.CLASS_NAME, value='property-listing')
            for data in raw_data:
                info = data.find_elements(By.CLASS_NAME, value='listing-item')
                img = data.find_element(By.CLASS_NAME, value="listing-image")


                temp_link = data.find_element(By.CLASS_NAME, value='btn')
                temp_link = temp_link.get_attribute('href')

                #btn= data.find_element(By.CSS_SELECTOR, value=)
                self.__built_dictionary(info)
                self.__property_data['Image'] = img.get_property('src')
                self.__property_data['Link'] = temp_link
                print(self.__property_data)

                self.__properties.append(self.__property_data.copy())
            try:
                next_btn = self.__driver.find_element(By.CLASS_NAME, value='pagination-next')

                if next_btn.is_enabled() and next_btn.is_displayed():
                    next_btn.click()
                else:
                    next_page=False
            except:
                next_page=False
        print(len(self.__properties),self.__properties)

    def update_data(self, data: list[dict]):
        url = self.__gsheet_url
        self.__driver.get(url)
        time.sleep(2)

        for info in data:
            #
            # Address/Location
            q1 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
            # Price
            q2 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Size
            q3 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Floor
            q4 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Year
            q5= self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')

            # Distance
            q6 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Link
            q7 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
            # Image Preview
            q8 = self.__driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
            click_btn = self.__driver.find_element(By.XPATH,
                                                   value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            #for info in data:
            q1.send_keys(info['Location'])
            q2.send_keys(info['Price'])
            q3.send_keys(info['Size'])
            q4.send_keys(info['Floor'])
            q5.send_keys(info['Year Built'])
            q6.send_keys(info['Distance'])
            q7.send_keys(info['Link'])
            q8.send_keys(info['Image'])
            click_btn.click()
            time.sleep(2)
            self.__driver.refresh()
            time.sleep(2)



    def add_entry(self, p_address, p_price, p_link):
        self.__properties.append({'Property_address': p_address,
                                  'Property_price': p_price,
                                  'Property_link': p_link})

    def __built_dictionary(self, item):
        global property_data
        self.__property_data['Location'] = item[0].text.replace('\n', ' ')
        price_filter = item[1].text.split(" ")[-1]
        price_filter = price_filter.replace('¥', '')
        price_filter = price_filter.replace(',', '')
        price_filter = float(price_filter)
        try:
            self.__property_data['Price'] = price_filter
            self.__property_data['Size'] = item[2].text.split(" ")[1]
            self.__property_data['Floor'] = item[3].text
            self.__property_data['Year Built'] = int(item[4].text.split(" ")[-1])
            self.__property_data['Distance'] = item[5].text
        except ValueError:
            self.__property_data['Floor'] = item[4].text
            self.__property_data['Year Built'] = int(item[5].text.split(" ")[-1])
            self.__property_data['Distance'] = item[6].text

    def get_properties_list(self):
        return self.__properties
