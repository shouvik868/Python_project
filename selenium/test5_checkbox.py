import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# chkbox_ele=driver.find_element(By.XPATH,"//input[@id='monday']")
# chkbox_ele.click()#checking one element
days_chekboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
#checking all the days
# for day in days_chekboxes:
#     day.click()
#     print("==========")
#     print(day.get_attribute("value"))
#selecting specific day
for day in days_chekboxes:
    day_name=day.get_attribute("value")
    if day_name!="sunday" and  day_name!="saturday":
       day.click()
       print(day_name)
       print("work on weekdays!!")
    else:
        print("Grab a beer on ",day_name)
for day in days_chekboxes:
    if day.is_selected():
        day.click()
    else:
        print("{} Not Selected!!".format(day.get_attribute("value")))


time.sleep(4)


driver.quit()
