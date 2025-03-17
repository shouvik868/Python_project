import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
select_ElementDD=driver.find_element(By.XPATH,"//select[@id='country']")
select=Select(select_ElementDD)
# select.select_by_visible_text("India")
# time.sleep(3)
# select.select_by_value("usa")
# time.sleep(3)
# select.select_by_index(2)
# time.sleep(3)
options=select.options
for option in options:
     print(option.text)
print(len(options))
driver.quit()


