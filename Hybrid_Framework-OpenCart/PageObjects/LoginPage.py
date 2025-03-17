from selenium.webdriver.common.by import By

class Loginpage:
    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,"input-email").send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.ID,"input-password").send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()