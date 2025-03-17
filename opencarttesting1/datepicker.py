import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

datepicker=driver.find_element(By.ID,'datepicker')
#approach 1
#datepicker.send_keys("09/12/1990")
#approach 2
datepicker.click()#clicking on textbox
# year="2025"
# month="September"
# Adate="12"

def afterDate(year,month,adate):
    while True:
        yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        mn = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        if year == yr and month == mn:
            break
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
    dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for date in dates:
        if date.text == adate:
            date.click()
            break
def beforeDate(year,month,adate):
    while True:
        yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        mn = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        if year == yr and month == mn:
            break
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
    dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for date in dates:
        if date.text == adate:
            date.click()
            break

#afterDate("2025","September","12")
#beforeDate("2024","February","12")
time.sleep(3)
driver.quit()