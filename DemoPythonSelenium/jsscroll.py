import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def click(element):
    time.sleep(3)
    driver.execute_script("arguments[0].click()",element)
    time.sleep(3)

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.execute_script("history.go(0)")
time.sleep(3)

driver.execute_script("window.scrollBy(0, 500)")
time.sleep(3)

driver.execute_script("history.go(0)")
time.sleep(3)

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(3)

driver.execute_script("window.scrollBy(0, -500)")
time.sleep(3)