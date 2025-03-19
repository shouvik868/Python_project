import time
import logging
import sys

import pytest
from  selenium import webdriver
from PageObjects.HomePage import Homepage
from PageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
sys.path.append("C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart")
from utilities import customLogger


customLogger.loggen().info("Welcome")
class TestLogin:


    @pytest.mark.sanity
    def test_valid_login(self,setup):
        customLogger.loggen().warning("welcome all")
        print("OK OK")

        self.driver=setup
        self.driver.get(ReadConfig.getAppURL())
        #self.logger.info("Hi")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        act_title=self.driver.title
        print("\n",act_title)
        if act_title=="Your Store":

            assert True
        else:

            self.driver.save_screenshot(
                "C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Screenshots/" + "Your_Store.png")
            self.driver.quit()
            assert False
        time.sleep(3)
        self.hp = Homepage(self.driver)
        self.hp.clickMyAcc()
        time.sleep(2)
        self.hp.clickLoginB()
        time.sleep(2)
        self.lp = Loginpage(self.driver)
        self.lp.setEmail(ReadConfig.getUserEmail())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()

        act_title2=self.driver.title
        if act_title2=="My Account":

            assert  True
        else:

            self.driver.save_screenshot(
                "C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Screenshots/" + "My_Account.png")
            self.driver.quit()
            assert  False
        print("\n",act_title2)

        self.driver.quit()

    @pytest.mark.sanity
    def test_invalid_login(self, setup):
        customLogger.loggen().warning("welcome all")
        print("OK OK")

        self.driver = setup
        self.driver.get(ReadConfig.getAppURL())
        # self.logger.info("Hi")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        print("\n", act_title)
        if act_title == "Your Store":

            assert True
        else:

            self.driver.save_screenshot(
                "C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Screenshots/" + "Your_Store.png")
            self.driver.quit()
            assert False
        time.sleep(3)
        self.hp = Homepage(self.driver)
        self.hp.clickMyAcc()
        time.sleep(2)
        self.hp.clickLoginB()
        time.sleep(2)
        self.lp = Loginpage(self.driver)
        self.lp.setEmail(ReadConfig.getInvalidUserEmail())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()

        act_title2 = self.driver.title
        if act_title2 == "My Account":
            self.driver.save_screenshot(
                "C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart/Screenshots/" + "My_Account.png")
            self.driver.quit()
            assert False
        else:
            assert True
        print("\n", act_title2)

        self.driver.quit()

