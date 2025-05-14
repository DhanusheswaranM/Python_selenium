import pytest
from Task2.Utils import ExcelReader
from Task2.Utils import read_config
from Task2.Pages.loginpage import LoginPage
data = ExcelReader.get_LoginData("D:/Python_selenium/Task2/Utils/LoginDataForOrangeHRM.xlsx","Sheet1")
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    # @pytest.mark.parametrize("username , password",ExcelReader.get_LoginData("D:/Python_selenium/Task2/Utils/LoginDataForOrangeHRM.xlsx","Sheet1"))
    def test_valid_Login(self):
        login_page = LoginPage(self.driver)
        username = read_config.get_config("login credentials","username")
        password = read_config.get_config("login credentials","password")
        login_page.set_Credentials(username,password)
        actual = login_page.get_DashboardText()
        expected = "Dashboard"
        assert actual==expected

    @pytest.mark.Invalid    
    @pytest.mark.parametrize("username , password",ExcelReader.get_LoginData("D:/Python_selenium/Task2/Utils/LoginDataForOrangeHRM.xlsx","Sheet1"))
    def test_invalid_login(self,username,password):
        login_page = LoginPage(self.driver)
        # username , password = data[1]
        login_page.set_Credentials(username,password)
        actual = login_page.get_errorText()
        expected = "Invalid credentials"
        assert actual==expected