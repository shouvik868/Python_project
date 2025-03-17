import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
def headless_chrome():
    options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)
    options.add_argument("__headless=new")
    options.add_argument("__window-size=1920,1080")
    driver_ch = webdriver.Chrome(options=options)
    return  driver_ch

def headless_firefox():
    options = webdriver.FirefoxOptions()
    #options.add_experimental_option("detach", True)
    #options.headless=True
    options.add_argument("__headless=new")
    driver_ff = webdriver.Firefox(options=options)
    return  driver_ff


#driver=headless_chrome()
driver=headless_firefox()
driver.get("http://ps.uci.edu/~franklin/doc/file_upload.html")
print(driver.title)
print(driver.current_url)
driver.quit()