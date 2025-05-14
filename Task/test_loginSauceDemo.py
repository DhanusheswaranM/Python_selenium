import pytest
from selenium.webdriver.common.by import By
import read_config
import time
import excelReader

data = excelReader.get_data("ExcelData/LoginData.xlsx","Sheet1")
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    @pytest.mark.parametrize('username , password',data)
    def test_valid(self,username,password):
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        if username == "standard_user" or username == "problem_user" or username == "performance_glitch_user":
            self.driver.find_element(By.XPATH,"//div[@class='bm-burger-button']/button").click()
            time.sleep(3)
            logout = self.driver.find_element(By.XPATH,"//div[@class='page_wrapper']/div[1]/div/div[2]/div[1]/nav/a[3]")
            assert logout.text == ("Logout")
            logout.click()
        if username == "locked_out_user":
            error = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
            print(error.text)
            assert error.text == "Epic sadface: Sorry, this user has been locked out."
        

    def test_standard_user(self):
        username , password = data[0]
        print(data[0])
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class='bm-burger-button']/button").click()
        time.sleep(3)
        logout = self.driver.find_element(By.XPATH,"//div[@class='page_wrapper']/div[1]/div/div[2]/div[1]/nav/a[3]")
        assert logout.text == ("Logout")
        logout.click()

    def test_locked_user(self):
        username , password = data[1]
        print(data[1])
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        error = self.driver.find_element(By.XPATH,"//h3[@data-test='error']")
        print(error.text)
        assert error.text == "Epic sadface: Sorry, this user has been locked out."            

    def test_problem_user(self):
        username , password = data[2]
        print(data[2])
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class='bm-burger-button']/button").click()
        time.sleep(3)
        logout = self.driver.find_element(By.XPATH,"//div[@class='page_wrapper']/div[1]/div/div[2]/div[1]/nav/a[3]")
        assert logout.text == ("Logout")
        logout.click()


    def test_performance_user(self):
        username , password = data[3]
        print(data[3])
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class='bm-burger-button']/button").click()
        time.sleep(3)
        logout = self.driver.find_element(By.XPATH,"//div[@class='page_wrapper']/div[1]/div/div[2]/div[1]/nav/a[3]")
        assert logout.text == ("Logout")
        logout.click()