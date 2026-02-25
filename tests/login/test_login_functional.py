import pytest
import re
from playwright.sync_api import expect

from pages.login.login_page import LoginPage


@pytest.mark.functional
class TestAdminLoginFunctional:

    def test_tc_01_verify_admin_login_ui_elements(self, page):
        """
        TC_01: Verify UI elements on Admin Login Page
        """
        login_page = LoginPage(page)
        login_page.navigate()
        page.wait_for_timeout(500)
        login_page.verify_ui_elements()
        page.wait_for_timeout(2000)
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

    #def test_tc_06_verify_remember_me_functionality(self, page):
    #    """
    #    TC_06: Verify LogIn with 'Keep me signed in for 30 days' checkbox
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.login_with_remember_me("chamika@ceydigital.com", "Qwer@#12345")
    #    expect(page.locator("div").nth(3)).to_be_visible() 

    #def test_tc_07_verify_password_visibility_toggle(self, page):
    #    """
    #    TC_04: Verify password visible icon functionality
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.password_input.fill("Qwer@#12345")
    #    assert login_page.get_password_field_type() == "password"
    #    login_page.toggle_password_visibility()
    #    page.wait_for_timeout(1000)
    #    assert login_page.get_password_field_type() == "text"
    #    login_page.toggle_password_visibility()
    #    page.wait_for_timeout(1000)
    #    assert login_page.get_password_field_type() == "password"
    #    page.wait_for_timeout(1000)

    #def test_tc_08_verify_theme_toggle_functionality(self, page):
    #    """
    #    TC_08: Verify theme toggle button functionality
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.click_theme_toggle()
    #    page.wait_for_timeout(1000)
    #    expect(login_page.theme_menu).to_be_visible()
    #    page.wait_for_timeout(2000)
    #
    #def test_tc_09_verify_theme_changes_to_light_mode(self, page):
    #    """
    #    TC_09: Verify Theme Changes to Light Mode
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.select_theme_light()
    #    page.wait_for_timeout(1000)
    #    expect(page.locator("html")).to_have_class(re.compile(r"light"))
    #    page.wait_for_timeout(1000)
    
    #def test_tc_10_verify_theme_changes_to_dark_mode(self, page):
    #    """
    #    TC_10: Verify Theme Changes to Dark Mode
    #    """
    #    login_page = LoginPage(page)
    #    login_page.navigate()
    #    login_page.select_theme_dark()
    #    page.wait_for_timeout(1000)
    #    expect(page.locator("html")).to_have_class(re.compile(r"dark"))
    #    page.wait_for_timeout(1000)
    
    def test_tc_11_verify_theme_changes_to_system_mode(self, page):
        """
        TC_11: Verify Theme Changes to System Mode
        """
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.select_theme_system()
        page.wait_for_timeout(1000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
