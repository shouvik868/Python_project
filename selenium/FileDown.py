import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()
def chromeSetUp():
    preference = {"download.default_directory": location} #in present working directory
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs",preference)
    driver_ch = webdriver.Chrome(options=options)
    return driver_ch

def edgeSetUp():
    preference = {"download.default_directory": location,"plugins.always_open_office_files_externally":True} #in present working directory
   #this is still open bug
    options = webdriver.EdgeOptions()
    #options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs",preference)
    driver_eg = webdriver.Edge(options=options)
    #driver_eg=webdriver.Edge()
    return driver_eg

def FFSetUp():

     options = webdriver.FirefoxOptions()
     #options.add_experimental_option("prefs",preference)
     options.set_preference("browser.download.folderList",2)
     options.set_preference("browser.download.dir",location)
     driver_ff = webdriver.Firefox(options=options)

     #driver_ff=webdriver.Firefox()
     return driver_ff

#driver=chromeSetUp()
driver=edgeSetUp()
#driver=FFSetUp()
# if driver==webdriver.Edge():
#     driver.get('edge://settings/downloads')
#     toggle = driver.execute_script('''
#                 return document.querySelector(' input[aria-label="Open Office files in
#         the browser"]');
#         ''')
#    toggle.click()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
print(driver.title)
driver.maximize_window()
download_link=driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='grippy-host']").click()
#download_link.location_once_scrolled_into_view
time.sleep(3)
download_link.click()
time.sleep(10)
#driver.quit()

