import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
driver=webdriver.Firefox()
driver.get("http://localhost/opencart/upload/index.php")
driver.maximize_window()
#driver.find_element(By.XPATH, "//a[@title='My Account']").click()
print("=====")
#print(driver.find_element(By.XPATH,"//a[text()='Login']").text)#getting text of the element
# driver.find_element(By.XPATH,"//a[text()='Login']").click()
# driver.find_element(By.ID,"input-email").send_keys("shouvikrcc@gmail.com")
# driver.find_element(By.ID,"input-password").send_keys("Password@123")
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
#time.sleep(5)#sleep time 5 sec
# driver.find_element(By.XPATH,"//a[@class='list-group-item'][normalize-space()='Newsletter']").click()
# driver.refresh()#refresh
# print(driver.title)
# driver.back()#backword
# print(driver.title)
# driver.forward()#forward
# print(driver.title)
# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
# print("=====")
# for link in links:
#     print(link.text)
#     print("=================")
#only getting footer links
footer_links=driver.find_elements(By.XPATH,"//footer//a")
print(len(footer_links))
for foo in footer_links:
    print(foo.text)
    print("==============")
