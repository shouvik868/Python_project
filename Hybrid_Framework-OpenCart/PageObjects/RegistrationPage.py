from selenium.webdriver.common.by import By

class Registrationpage:
    def __init__(self,driver):
        self.driver=driver

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,"input-firstname").send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.ID,"input-lastname").send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.ID,"input-email").send_keys(email)

    def setTelephone(self,pnumber):
        self.driver.find_element(By.ID,"input-telephone").send_keys(pnumber)

    def setPassword(self,pwd):
        self.driver.find_element(By.ID,"input-password").send_keys(pwd)

    def setPasswordConfirmation(self,pwd_conf):
        self.driver.find_element(By.ID,"input-confirm").send_keys(pwd_conf)

    def clickPolicy(self):
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()

    def getmsgConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        except:
            print("No message found!!")


