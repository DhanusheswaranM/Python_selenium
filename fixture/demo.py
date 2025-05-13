from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = None 

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.html")

def teardown_function(function):
    global driver
    driver.quit()


def test_Hard_Assert():
    global driver
    username_text = driver.find_element(By.XPATH,"//div[@id='loginPanel']/form/p")
    username = driver.find_element(locate_with(By.TAG_NAME,"input").below(username_text))
    username.send_keys("Dhanush")

    loginBtn = driver.find_element(By.XPATH,"//div[@id='loginPanel']/form/div[3]/input")
    password = driver.find_element(locate_with(By.TAG_NAME,"input").above(loginBtn))
    password.send_keys("Dhanush2412$")

    loginBtn.click()

    expected = "The username and password could not be verified."
    actualText = driver.find_element(By.XPATH,"//div[@id='rightPanel']/p").text
    assert expected.__contains__(actualText)

def test_Soft_Assert():
    global driver
    forgot_login_info = driver.find_element(By.XPATH,"//div[@id='loginPanel']/p[1]")

    register_btn = driver.find_element(locate_with(By.TAG_NAME,"a").below(forgot_login_info))
    register_btn.click()

    username_text = driver.find_element(By.XPATH,"//div[@id='loginPanel']/form/p")
    username = driver.find_element(locate_with(By.TAG_NAME,"input").below(username_text))
    username.send_keys("Dhanush")

    loginBtn = driver.find_element(By.XPATH,"//div[@id='loginPanel']/form/div[3]/input")
    password = driver.find_element(locate_with(By.TAG_NAME,"input").above(loginBtn))
    password.send_keys("Dhanush2412$")

    loginBtn.click()

    request_Loan = driver.find_element(By.XPATH,"//div[@id='leftPanel']/ul/li[7]")
    logout = driver.find_element(locate_with(By.TAG_NAME,"a").near(request_Loan))
    time.sleep(3)
    if logout.text.__contains__("logout"):
        print("Login was successful")
    else:
        print("Login was not successfull ")