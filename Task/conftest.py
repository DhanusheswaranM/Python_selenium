import pytest
from selenium import webdriver
import read_config
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic", "browser")
    driver = None
    if browser.__eq__("chrome"):
        chrome_options=Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        chrome_options.add_argument("--incognito")
        driver=webdriver.Chrome(options=chrome_options)

        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("the browser not not valid")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = read_config.get_config("basic","url")
    driver.get(url)

    request.cls.driver = driver

    yield
    driver.quit()
