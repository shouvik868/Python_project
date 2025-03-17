import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")
#driver.get("https://testautomationpractice.blogspot.com/")
links = driver.find_elements(By.TAG_NAME, "a")
print("total links: ", len(links))
count = 0
for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print("Broken link:", url)
        count += 1
    else:
        print(url, " is good!!")


print("Total number of broken links are: ", count)

driver.quit()
