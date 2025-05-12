import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

parentWindow_Id=driver.current_window_handle

driver.find_element(By.LINK_TEXT,"Open a popup window").click()
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
windowsId=driver.window_handles

for w in windowsId:
    driver.switch_to.window(w)
    if "New Window" in driver.title:
        print("inside if")
        window_text=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
        print(window_text)
        driver.close()
        break
time.sleep(5)

driver.switch_to.window(parentWindow_Id)
print(driver.title)
driver.close()
driver.quit()