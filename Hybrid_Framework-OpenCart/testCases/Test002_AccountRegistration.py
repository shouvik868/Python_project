import time
import pytest
from  selenium import webdriver
import  sys
from PageObjects.HomePage import Homepage
from PageObjects.RegistrationPage import Registrationpage
from utilities.readProperties import ReadConfig
sys.path.append("C:/Users/HP/PycharmProjects/seleniumProject/Hybrid_Framework-OpenCart")
from utilities import customLogger
from utilities import Random_Generator

class TestRegistration:
    customLogger.loggen().info("hi o")

    @pytest.mark.sanity
    #@pytest.mark.regression
    def test_acc_registration(self,setup):
        customLogger.loggen().info("Welcome")
        print("OK OK")

        self.driver=setup
        self.driver.get(ReadConfig.getAppURL())
        #self.logger.info("Hi")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        act_title=self.driver.title
        print("\n",act_title)
        time.sleep(3)
        #home page
        self.hp = Homepage(self.driver)
        self.hp.clickMyAcc()
        time.sleep(2)
        self.hp.clickRegister()
        time.sleep(2)
        #registration page
        title_reg=self.driver.title
        print("\n",title_reg)
        self.rp = Registrationpage(self.driver)
        self.rp.setFirstname(Random_Generator.random_fname_generator())
        time.sleep(2)
        self.rp.setLastname(Random_Generator.random_lname_generator())
        time.sleep(2)
        self.rp.setEmail(Random_Generator.random_email_generator()+"@gmail.com")
        self.rp.setTelephone("9830174563")
        self.rp.setPassword("Password@123")
        time.sleep(2)
        self.rp.setPasswordConfirmation("Password@123")
        time.sleep(2)
        self.rp.clickPolicy()
        time.sleep(2)
        self.rp.clickSubmit()
        time.sleep(2)
        conf_msg=self.rp.getmsgConfirmation()
        if conf_msg=="Your Account Has Been Created!":
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.quit()
