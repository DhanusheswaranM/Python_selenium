import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.co.in")

def teardown_function(function):
    driver.quit()

@pytest.mark.parametrize("search_term", [('Selenium'), ('pytest')])
def test_search_google(search_term):
    driver.find_element(By.NAME, value="q").send_keys(search_term)
    time.sleep(5)
    driver.find_element(By.NAME,"btnK").click()

