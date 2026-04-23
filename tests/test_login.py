import pytest
import allure

from pages.login_page import LoginPage
from utilities.assertion_helpers import AssertionHelpers
from config.credentials import Credentials


@allure.feature("Login Tests")
@allure.title("Verify successful login with valid credentials")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open_page()

    with allure.step("Login using valid credentials"):
        login_page.login(
            Credentials.EMAIL,
            Credentials.PASSWORD
        )

    with allure.step("Verify Dashboard is displayed after login"):
        actual_text = login_page.get_element_text(
            login_page.dashboard_locator
        )

        AssertionHelpers.assert_text_contains(
            actual_text,
            "Dashboard"
        )



@pytest.mark.skip(reason="Test is currently unstable due to recent UI changes")
@allure.feature("Login Tests")
@allure.title("Verify login fails with invalid password")
@allure.story("Failed Login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open_page()

    with allure.step("Login using invalid password"):
        login_page.login(
            Credentials.EMAIL,
            "wrong_password"
        )

    with allure.step("Verify invalid password message is shown"):
        actual_message = login_page.get_element_text(
            login_page.message_locator
        )

        AssertionHelpers.assert_text_contains(
            actual_message,
            "Incorrect password"
        )

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
