import time
import logging

import pytest
from  selenium import webdriver
import  sys
# sys.path.append("C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/PageObjects")
from PageObjects.HomePage import Homepage
from PageObjects.LoginPage import Loginpage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGenerator
from utilities import XLUtils


class TestLogin_ddt_02:

    data_path="C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/TestData/Opencart_login_data.xlsx"
    #logger=LogGenerator.loggen()
    #@pytest.mark.regression
    @pytest.mark.regression
    def test_valid_login_2(self,setup):
        #self.logger.info("Hii")
        print("OK OK")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = Loginpage(self.driver)
        time.sleep(5)
        self.rows=XLUtils.getRowCount(self.data_path,"py_login")
        print("row count",self.rows)

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.data_path,"py_login",r,1)
            self.password = XLUtils.readData(self.data_path, "py_login", r, 2)
            #self.exp = XLUtils.readData(self.data_path, "py_login", r, 3) 

            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == "My Account":

                print("Correct")
            else:

                self.driver.save_screenshot(
                    "C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Screenshots/" + "My_Account.png")
                self.driver.quit()
                print("Incorrect")
                break
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()


