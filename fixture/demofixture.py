import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search:
    def test_valid_product(self):
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("HP")
        self.driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
        expected = self.driver.find_element(By.LINK_TEXT,"HP LP3065")
        assert expected.is_displayed()

    def test_invalid_product(self):
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
        expected = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//div[@id='content']/p[2]").text
        assert actual.__eq__(expected)

    def test_empty_product(self):
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("")
        self.driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
        expected = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//div[@id='content']/p[2]").text
        assert actual.__eq__(expected)
