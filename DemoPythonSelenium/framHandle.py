import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://letcode.in/frame")

# driver.switch_to.frame("firstFr")

# driver.find_element(By.NAME,"fname").send_keys("Dhanush")
# driver.find_element(By.NAME,"lname").send_keys("M")

# # driver.switch_to.frame(1)
# time.sleep(3)
# driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='container has-text-centered mb-4 mt-6']//iframe"))
# driver.find_element(By.NAME,"email").send_keys("mdhanusheswaran@gmail.com")

# driver.switch_to.parent_frame()
# driver.find_element(By.NAME,"lname").clear()

driver.get("https://omayo.blogspot.com/")

driver.switch_to.frame("navbar-iframe")

driver.find_element(By.CLASS_NAME,"ENqPLc").send_keys("Selenium")
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='m3Blcf opT0zc']").click()

driver.switch_to.parent_frame()

text=driver.find_element(By.XPATH,"(//div[@class='status-msg-body'])[1]")
print(text.text)