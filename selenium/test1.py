from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("http://localhost/opencart/upload/index.php")
print(driver.title)
print(driver.current_url)
print("=============")
#print(driver.page_source)

if driver.find_element(By.XPATH,"//button[@class='btn btn-link dropdown-toggle']").is_displayed():
    print("displayed")




driver.quit()