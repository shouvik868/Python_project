from selenium.webdriver.common.by import By
from selenium import webdriver

class Homepage:
    def __init__(self,driver):
        self.driver=driver


    # buttonMyAccount = (By.XPATH,"//span[contains(text(),'My Account')]")
    # buttonRegister = (By.XPATH,"//a[contains(text(),'Register')]")
    # buttonLogin = (By.XPATH,"//a[contains(text(),'Login')]")

    def clickMyAcc(self):
        #self.driver.find_element(self.buttonMyAccount).click()
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
    def clickRegister(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()

    def clickLoginB(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()

