import time
from selenium import webdriver
from selenium.webdriver.common.by import By   

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.google.com")
driver.get("https://selenium08.blogspot.com/2019/07/check-box-and-radio-buttons.html")

# print("The title of the web page is :",driver.title,"is",driver.title.__contains__("Google"))
# time.sleep(3)
# search_box=driver.find_element(By.ID,value="APjFqb")
# print("Search box is enabled : ",search_box.is_enabled())
# time.sleep(3)
# search_box.send_keys("Selenium")
# time.sleep(3)
# search_btn=driver.find_element(By.NAME,value="btnK")
# print("Search button is enabled : ",search_btn.is_enabled())
# time.sleep(3)
# search_btn.click()
# time.sleep(5)

red_box=driver.find_element(By.XPATH,"//div[@id='post-body-7702345506409447484']/div/input[1]")
print("Red check box is enabled :",red_box.is_enabled())
print("check the red box is selected :",red_box.is_selected())
red_box.click()
print("check the red box is selected after clicking it :",red_box.is_selected())
opera_box=driver.find_element(By.XPATH,"//div[@id='post-body-7702345506409447484']/div/div/input[3]")
print("check the opera radial button is selected :",opera_box.is_selected())