import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
driver=webdriver.Edge()
driver.implicitly_wait(3)
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='gender-male']").click()

if driver.find_element(By.XPATH,"//input[@id='gender-male']").is_selected():
    print("Selected")
if driver.find_element(By.XPATH,"//input[@id='gender-male']").is_enabled():
    print("Enabled")
    if driver.find_element(By.XPATH, "//input[@id='gender-female']").is_selected():
        print("Selected")
    else:
        print("not Selected")

