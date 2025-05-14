import pytest
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field_name("HP")
        home_page.click_search_button()
        
        search_page = SearchPage(self.driver)
        search_page.display_status_of_valid_product()