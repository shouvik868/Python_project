import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://www.orangehrm.com/")
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(5)
cur_wnd_id=driver.current_window_handle
print(cur_wnd_id)
#scroll into View
driver.find_element(By.XPATH,"(//div[@class='social-icon'])[1]").location_once_scrolled_into_view
time.sleep(4)
driver.find_element(By.XPATH,"(//div[@class='social-icon'])[1]").click()
wind_ids=driver.window_handles
parent=wind_ids[0]
child=wind_ids[1]
print("parent: ",parent)
print("================")
print("child: ",child)
print("================")
driver.switch_to.window(child)
time.sleep(4)
driver.find_element(By.XPATH,"//div[@aria-label='Close']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(parent)
time.sleep(4)
driver.find_element(By.XPATH,"(//div[@class='social-icon'])[2]").click()
time.sleep(2)
driver.quit()