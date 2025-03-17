from selenium import webdriver
from selenium.webdriver.common.by import By
Options=webdriver.ChromeOptions()
Options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=Options)
driver.get("http://localhost/opencart/upload/index.php")
print(driver.title)
driver.maximize_window()
driver.get("https://www.youtube.com/")