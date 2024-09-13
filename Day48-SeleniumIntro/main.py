from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

'''
Other options
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
'''

# print(f"Price dollars ${price_dollar.text}.{price_cents.text}")



#Docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#print(Docs_link.text)

# Location by XPATH

#driver.get("https://python.org/")
# events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# print(events.text)

# my_dict={}
#
# for i in range(0,len(lines),2):
#     print(i)
#     my_dict[lines[i]] = lines[i+1]

# keys = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# values = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
#
# my_dict = {n: {'time' : keys[n].text , 'name': values[n].text} for n in range(len(keys))}
#
# print(my_dict)
name = driver.find_element(By.NAME, value="fName")
last = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
click_btn= driver.find_element(By.XPATH, value='/html/body/form/button')

name.send_keys("first")
last.send_keys("last")
email.send_keys("email@fake.com")

click_btn.click()


#driver.quit()