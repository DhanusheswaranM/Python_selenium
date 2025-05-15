from selenium.webdriver.common.by import By
from .BasePage import Action

class DashboardPage:

    def __init__(self,driver):
        self.driver = driver
        self.leave = (By.XPATH,"//ul[@class='oxd-main-menu']/li[3]/a/span")
        self.time = (By.XPATH,"//ul[@class='oxd-main-menu']/li[4]/a/span")

    def get_leave(self):
        leave_text = self.driver.find_element(*self.leave)

        return Action.get_text(leave_text)

    def get_time(self):
        time_text = self.driver.find_element(*self.time)

        return Action.get_text(time_text)