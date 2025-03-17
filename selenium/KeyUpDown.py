import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://text-compare.com/")
#input box 1
input1=driver.find_element(By.XPATH,"//textarea[@name='text1']")
#input box 2
input2=driver.find_element(By.XPATH,"//textarea[@name='text2']")

#write something in input area 1
input1.send_keys("Welcome Shouvik!!")

action=ActionChains(driver)
#select text input 1
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#copy text input 1
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#move totext area 2 and click
action.move_to_element(input2).click().perform()
#paste text input 2
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(3)
driver.quit()
