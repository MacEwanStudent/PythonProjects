from selenium import webdriver
from selenium.webdriver.common.by import By

real_sate_endpoint = "https://realestate.co.jp/en/forsale/listing?prefecture=JP-13&city=&trainline=11302&station=1130203&min_cap_rate=&min_price=&max_price=&min_meter=&rooms=&distance_station=&agent_id=&building_type=mansion-apartment&building_age=&updated_within=&transaction_type=&occupancy=&order=&search=Search&page=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=chrome_options)
driver.get(real_sate_endpoint)

raw_data =driver.find_elements(By.CLASS_NAME, value='property-listing')
property_data = {
    'Location': "",
    'Price': 0.0,
    'Size': "",
    'Floor': "",
    'Year Built': 0,
    'Link': "",
    'Distance': "",
    'Image': ""
}



    # for item in price:
    #
    #     print(n, item.text)
    #     n+=1


def get_info(item):
    global property_data
    property_data['Location']=item[0].text.replace('\n', ' ')
    price_filter = item[1].text.split(" ")[-1]
    price_filter = price_filter.replace('¥', '')
    price_filter = price_filter.replace(',','')
    price_filter = float(price_filter)
    property_data['Price'] = price_filter
    property_data['Size'] = item[2].text.split(" ")[1]
    property_data['Floor'] = item[3].text
    property_data['Year Built'] = int(item[4].text.split(" ")[-1])
    property_data['Distance'] = item[5].text


for index in range(3):
    data = raw_data[index]
    info = data.find_elements(By.CLASS_NAME, value='listing-item')
    img= data.find_element(By.CLASS_NAME, value="listing-image")
    property_data['Image']= img.get_property('src')
    n = 0
    get_info(info)
    print(property_data)

