from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

driver.implicitly_wait(8)
english_btn= driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
english_btn.click()
driver.implicitly_wait(10)
cookie_btn= driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')

update_box = driver.find_element(By.ID, value="store")

cookies = driver.find_element(By.ID, value='cookies')

n = 1
cookie_points = 0
while (n < 1000):
    if (n % 100) == 0:
        update_option = update_box.find_elements(By.CLASS_NAME, value="product")
        cookies = driver.find_element(By.XPATH, value='//*[@id="cookies"]')
        cookie_points = int(cookies.text.split(" ")[0])
        print("Cookie points", cookie_points)

        for update in update_option:
            num = update.text.split('\n')[-1]
            if num.isdigit():
                diff = cookie_points // int(num)
                print("DIFF", diff)
                if (diff > 0) and (diff < 50):
                    for i in range(diff):
                        update.click()

    try:
        cookie_btn.click()
    except:
        cookie_btn = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
        time.sleep(1)
    time.sleep(0.05)
    print(n)
    n += 1