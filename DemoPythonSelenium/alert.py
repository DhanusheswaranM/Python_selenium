import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//div[@id='content']/div/ul/li[1]/button").click()
simplealert=driver.switch_to.alert
time.sleep(3)
print(simplealert.text)
simplealert.accept()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='content']/div/ul/li[2]/button").click()
confirmalert=driver.switch_to.alert
time.sleep(3)
print(confirmalert.text)
confirmalert.accept()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='content']/div/ul/li[3]/button").click()
promptalert=driver.switch_to.alert
time.sleep(3)
print(promptalert.text)
promptalert.send_keys("welcome")
time.sleep(3)
promptalert.accept()
time.sleep(3)