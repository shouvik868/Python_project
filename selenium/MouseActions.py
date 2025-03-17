import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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
time.sleep(3)
ele_desktop=driver.find_element(By.XPATH,"(//a[@class='dropdown-toggle'])[2]")
ele_mac=driver.find_element(By.XPATH,"(//a[contains(text(),'Mac')])[1]")
time.sleep(3)
#ActionChain class
actions=ActionChains(driver)
actions.move_to_element(ele_desktop).move_to_element(ele_mac).click().perform()
