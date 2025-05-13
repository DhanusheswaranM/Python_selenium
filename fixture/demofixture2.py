import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search:
    def test_search(self):
        time.sleep(3)
        search = self.driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
        search.send_keys("selenium")
        time.sleep(5)
        searchBtn =  self.driver.find_element(By.NAME,"btnK")
        searchBtn.click()