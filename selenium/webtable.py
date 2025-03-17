import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("==================")
rowcount=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
print(rowcount-1)
print("==================")
colcount=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
print(colcount)
print("==================")
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[1]").text
# print(data)
#getting all data from a table
for r in range(2,rowcount+1):
     for c in range(1,colcount+1):
        value=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='            ')
     print()

#playing with for loop
print("======books by Mukesh========")
for r in range(2,rowcount+1):
    author=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text

    if author=="Mukesh":
        book=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print("{} by {} worth {} INR only!!".format(book,author,price))
driver.quit()