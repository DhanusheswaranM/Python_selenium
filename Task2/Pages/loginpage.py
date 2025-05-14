from selenium.webdriver.common.by import By
from .BasePage import Action

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.pwrd = (By.NAME, "password")
        self.loginBtn = (By.XPATH, "//form[@class='oxd-form']/div[3]/button")
        self.dashboard_text = (By.XPATH,"//div[@class='oxd-topbar-header-title']/span/h6")
        self.error = (By.XPATH,"//div[@role='alert']/div/p")

    def set_Credentials(self, uname: str, password: str):
        user_input = self.driver.find_element(*self.username)
        pwrd_input = self.driver.find_element(*self.pwrd)
        login_button = self.driver.find_element(*self.loginBtn)

        Action.sendKeys(user_input, uname)
        Action.sendKeys(pwrd_input, password)
        Action.click(login_button)
    
    def get_DashboardText(self):
        element = self.driver.find_element(*self.dashboard_text)
        return Action.get_text(element)
    
    def get_errorText(self):
        element = self.driver.find_element(*self.error)
        return Action.get_text(element)