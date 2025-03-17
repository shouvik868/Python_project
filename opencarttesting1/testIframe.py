import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
# frames=driver.find_elements(By.TAG_NAME,'iframe')
# print(len(frames))
#driver.find_element(By.XPATH,"//a[normalize-space()='Single Iframe']").click()
time.sleep(3)
#driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']"))#frame as webelement
driver.switch_to.frame("SingleFrame")#frame name or index
text_ele=driver.find_element(By.XPATH,"//input[@type='text']")
text_ele.send_keys("Tubai")
time.sleep(3)
driver.switch_to.default_content()#out of frame
#driver.switch_to.parent_frame()#to parent frame
driver.quit()