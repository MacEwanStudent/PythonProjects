from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://www.amazon.ca/Tassimo-Nabob-Espresso-Single-T-Discs/dp/B06X93NNZ7?pd_rd_w=AtPxB&content-id=amzn1.sym.d66add78-05b0-4a3d-9404-5c9bc639cee0&pf_rd_p=d66add78-05b0-4a3d-9404-5c9bc639cee0&pf_rd_r=PSH2KQ1C337TVHR5KBWV&pd_rd_wg=pkOms&pd_rd_r=aab8e43e-b540-4143-a39b-b22bd119c59e&pd_rd_i=B06X93NNZ7&ref_=pd_bap_d_grid_rp_0_1_ec_scp_pd_hp_d_atf_rp_1_i&th=1"

# Keep web browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is ${price_dollar.text}.{price_cents.text}")

# driver.close()
driver.quit()

