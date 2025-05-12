import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize("search_term",[("selenium"), "java", ("selenium locators")])
# def test_google_search(search_term):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.co.in/")

#     driver.find_element(By.NAME,'q').send_keys(search_term)
#     time.sleep(5)

#     driver.find_element(By.NAME,"btnK").click()

@pytest.mark.parametrize("browser",["chrome","firefox"])
@pytest.mark.parametrize("url",["https://www.flipkart.com/","https://www.amazon.in/"])
def test_browser(browser , url):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    if browser == "firefox" :
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    print(driver.title)
    driver.quit()