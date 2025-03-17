import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Options=webdriver.ChromeOptions()
Options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=Options)
driver.get("https://swisnl.github.io//jQuery-contextMenu/demo.html")
print(driver.title)
driver.maximize_window()
ele_button=driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
ele_paste=driver.find_element(By.XPATH,"//span[normalize-space()='Paste']")
time.sleep(3)
action=ActionChains(driver)
action.move_to_element(ele_button).context_click().move_to_element(ele_paste).click().perform()
time.sleep(3)
driver.quit()
#other ActionChain method
#action.double_click(element)
#action.drag_and_drop(source,target)
#action.drag_and_drop_by_offset(slider,x,0)#for slider
#java script slider
# driver.execute("window.scrollBy(0,3000)","")***
# value=driver.execute_script("return window.pageYOffset;")
# print(value)
#scroll till element
#driver.execute_script("arguments[0].scrollIntoView();","Element")
