import pytest
from selenium.webdriver.common.by import By
from Utilities.consolelogger import get_logger
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_product(self):
        logger = get_logger()
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field_name("HP")
        logger.info("The product is entered to search")
        home_page.click_search_button()
        
        search_page = SearchPage(self.driver)
        search_page.get_display_status_of_valid_product()
        logger.info("The product is displayed correctly")