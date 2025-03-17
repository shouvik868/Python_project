import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://ps.uci.edu/~franklin/doc/file_upload.html")
#always look for the input tag :)
driver.find_element(By.XPATH,"//input[@name='userfile']").send_keys("C:/Users/HP/Desktop/new_framework_2025/Python/file_to_upload.doc")
time.sleep(3)
driver.quit()




