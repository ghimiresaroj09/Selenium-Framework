from pages.login_page import LoginPage
from utilities.excel_utils import read_excel_data
from utilities.screenshot_utils import ScreenshotUtils
from config.credentials import Credentials
import pytest


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(Credentials.EMAIL, Credentials.PASSWORD)
    
    # Take screenshot after successful login
    ScreenshotUtils.take_screenshot(driver, "login_success")
    
    assert "Dashboard" in login_page.get_element_text(login_page.dashboard_locator)


# test_data = read_excel_data("test_data/Login_data.xlsx")

# @pytest.mark.parametrize("login_data",test_data)
# def test_login(driver,login_data):
#     login_page = LoginPage(driver)
#     login_page.open_page()
#     login_page.login(
#         login_data["Email"],
#         login_data["Password"]
#     )
#     login_page.get_element_text(login_page.message_locator) == "Successfully signin"
