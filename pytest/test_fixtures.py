import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setUp_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    yield
    driver.quit()

def test_valid_product(test_setUp_and_teardown):
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("HP")
    driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
    expected =driver.find_element(By.LINK_TEXT,"HP LP3065")
    assert expected.is_displayed()

def test_invalid_product(test_setUp_and_teardown):
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("Honda")
    driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
    expected = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH,"//div[@id='content']/p[2]").text
    assert actual.__eq__(expected)

def test_empty_product(test_setUp_and_teardown):
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("")
    driver.find_element(By.XPATH,"//span[@class='input-group-btn']/button").click()
    expected = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH,"//div[@id='content']/p[2]").text
    assert actual.__eq__(expected)