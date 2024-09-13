from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url="https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_num = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(article_num.text)
#article_num.click()
# all_portals= driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()
#//*[@id="p-search"]/a/span[1]
open_search = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
open_search.click()

driver.implicitly_wait(2)
#//*[@id="searchform"]/div/div/div[1]/input
search = driver.find_element(By.XPATH, value='//*[@id="searchform"]/div/div/div[1]/input')
search.send_keys("Python")
#driver.quit()
