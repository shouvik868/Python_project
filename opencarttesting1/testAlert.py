import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.XPATH,"//*[text()='Simple Alert']").click()
# time.sleep(3)
# driver.switch_to.alert.accept()
# driver.find_element(By.XPATH,"//*[text()='Confirmation Alert']").click()
# time.sleep(3)
# driver.switch_to.alert.dismiss()
# driver.find_element(By.XPATH,"//*[text()='Prompt Alert']").click()
# time.sleep(3)
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.send_keys("Tom")
# time.sleep(3)

#url-injection for authenticated popups
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
driver.quit()


