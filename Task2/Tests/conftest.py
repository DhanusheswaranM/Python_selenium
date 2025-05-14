import pytest
from selenium import webdriver
from Task2.Utils import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic info","browser")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("There is no valid browser")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = read_config.get_config("basic info","url")
    driver.get(url)

    request.cls.driver = driver 

    yield
    driver.quit()
    