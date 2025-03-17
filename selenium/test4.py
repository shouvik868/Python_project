
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
driver=webdriver.Firefox()
#driver.implicitly_wait(3)
explicite_wait=WebDriverWait(driver,5,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,Exception])
#Explicite wait declarations
driver.get("http://localhost/opencart/upload/index.php")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@title='My Account']").click()
driver.find_element(By.XPATH,"//a[text()='Login']").click()
print("=====")
email_element=explicite_wait.until(EC.presence_of_element_located((By.ID,"input-email")))#explicite wait
attr_value=email_element.get_attribute("placeholder")
print(attr_value)
driver.quit()
