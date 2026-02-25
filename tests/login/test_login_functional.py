import pytest
from playwright.sync_api import expect

from pages.login.login_page import LoginPage


@pytest.mark.functional
class TestAdminLoginFunctional:

    # def test_tc_01_verify_admin_login_ui_elements(self, page):
    #    """
    #    TC_01: Verify UI elements on Admin Login Page
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    page.wait_for_timeout(500)
    #    login_page.verify_ui_elements()
    #    page.wait_for_timeout(1000)
    #
    # def test_tc_02_verify_successful_login(self, page):
    #    """
    #    TC_02: Verify Successful LogIn
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    page.wait_for_timeout(500)
    #    login_page.login("chamika@ceydigital.com", "Qwer@#12345")
    #    page.wait_for_timeout(500)
    #    expect(page.locator("div").nth(3)).to_be_visible()
    #    page.wait_for_timeout(500)
    #
    # def test_tc_03_verify_login_with_invalid_credentials(self, page):
    #    """
    #    TC_03: Verify LogIn with Invalid Credentials
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.login("chamika@ceydigital.com", "Qwer@#123455")
    #    login_page.verify_login_error_is_displayed()
    #    page.wait_for_timeout(500)

    # def test_tc_04_verify_login_with_invalid_email_format(self, page):
    #    """
    #    TC_04: Verify LogIn with Invalid email format
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.login("chamika#ceydigital.com", "Qwer@#12345")
    #    error_message = login_page.get_email_validation_message()
    #    page.wait_for_timeout(1000)
    #    assert error_message != "", "Email validation message is not displayed!"
    #    page.wait_for_timeout(1000)

    #def test_tc_05_verify_login_with_empty_fields(self, page):
    #    """
    #    TC_05: Verify LogIn with Empty field
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.sign_in_btn.click()
    #    email_error = login_page.get_email_validation_message()
    #    page.wait_for_timeout(1000)
    #    pass_error = login_page.get_password_validation_message()
    #    page.wait_for_timeout(1000)
    #    assert (
    #        email_error != "" or pass_error != ""
    #    ), "Validation message not shown for empty fields!"
    #    page.wait_for_timeout(1000)

    def test_tc_06_verify_remember_me_functionality(self, page):
        """
        TC_06: Verify LogIn with 'Keep me signed in for 30 days' checkbox
        """
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login_with_remember_me("chamika@ceydigital.com", "Qwer@#12345")
        expect(page.locator("div").nth(3)).to_be_visible() 
