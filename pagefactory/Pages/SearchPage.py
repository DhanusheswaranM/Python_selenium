from selenium .webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver 

    # display_status_of_valid_product_link_text = "HP LP3065"

    # def display_status_of_valid_product(self):
    #     return self.driver.find_element(By.LINK_TEXT,self.display_status_of_valid_product_link_text).is_displayed()
    locators ={
        'display_status_of_valid_product_link_text':('xpath',"//a[text()='HP LP3065']")
    }
    
    def get_display_status_of_valid_product(self):
        assert self.display_status_of_valid_product_link_text.is_displayed()
        assert self.display_status_of_valid_product_link_text.get_text() == "HP LP3065"