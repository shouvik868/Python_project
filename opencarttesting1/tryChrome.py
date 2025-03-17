from selenium import webdriver
from selenium.webdriver.common.by import By
Options=webdriver.ChromeOptions()
Options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=Options)
driver.get("http://localhost/opencart/upload/index.php")
print(driver.title)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@title='My Account']").click()
driver.find_element(By.XPATH,"//a[text()='Login']").click()
driver.find_element(By.ID,"input-email").send_keys("shouvikrcc@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("Password@123")
driver.find_element(By.XPATH,"//input[@value='Login']").click()
print(driver.title)
#driver.close()

