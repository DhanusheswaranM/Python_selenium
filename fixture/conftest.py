# from pickle import TRUE
import pytest
from selenium import webdriver

# @pytest.fixture()
# def setUp_and_teardown():
#     # global driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     # driver.get("https://tutorialsninja.com/demo/")
#     driver.get("https://www.google.co.in/")
#     # request.cls.driver = driver

#     yield
#     driver.quit()

@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup_and_teardown(request):
    if request.param == "chrome":
        driver=webdriver.Chrome()
    elif request.param == "firefox":
        driver=webdriver.Firefox()
    elif request.param == "edge":
        driver=webdriver.Edge()
    driver.maximize_window()
    # driver.get("https://tutorialsninja.com/demo/")
    driver.get("https://www.google.co.in/")
    # request.cls.driver = driver

    yield
    driver.quit()