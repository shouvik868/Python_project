from selenium import webdriver
from selenium.webdriver.common.by import By
# Options=webdriver.ChromeOptions()
# Options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=Options)
driver=webdriver.Firefox()

#driver.get("https://demo.nopcommerce.com/")
#using different locators
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.LINK_TEXT,'Register').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'ter').click()
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
#sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
#print(len(sliders))#5
#print(type(sliders))#list
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))#88


