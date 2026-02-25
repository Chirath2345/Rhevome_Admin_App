import re

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # --- UI Element Locators (TC_01) ---
        self.logo = page.get_by_role("img", name="Rhevome Logo")
        self.theme_toggle_btn = page.get_by_role("button", name="Toggle theme")
        self.admin_portal_header = page.get_by_text("Admin Portal")
        self.portal_subtext = page.get_by_text("Sign in to access your secure")

        # Input Labels
        self.email_label = page.get_by_text("Email Address")
        self.password_label = page.get_by_text("Password", exact=True)

        # Input Fields
        self.email_input = page.get_by_role("textbox", name="Email Address")
        self.password_input = page.get_by_role("textbox", name="Password")

        # Interactive Elements
        # Password eye icon/button filter ekak damma empty role ekak ena nisa
        self.password_toggle_btn = page.get_by_role("button").filter(
            has_text=re.compile(r"^$")
        )
        self.remember_me_checkbox = page.locator("div").filter(
            has_text=re.compile(r"^Keep me signed in for 30 days$")
        )
        self.sign_in_btn = page.get_by_role("button", name="Sign In")

        # HIPAA Notice
        self.hipaa_notice = page.get_by_text("This system contains")

        # Login button
        self.sign_in_btn = page.get_by_role("button", name="Sign In")

        # Login Error messages
        self.error_toast_list = page.get_by_role("listitem")
        self.login_failed_msg = page.get_by_text("Login Failed")
        self.invalid_credentials_msg = page.get_by_text("Invalid credentials")

        self.email_error_msg = page.get_by_text("Please enter a valid email")

        self.remember_me_checkbox = page.get_by_role(
            "checkbox", name="Keep me signed in for 30 days"
        )

        self.password_toggle_btn = page.get_by_role("button").filter(has_text=re.compile(r"^$"))
        self.theme_toggle_btn = page.get_by_role("button", name="Toggle theme")
        self.theme_menu = page.get_by_role("menu", name="Toggle theme")
        self.light_theme_item = page.get_by_role("menuitem", name="Light")
        self.dark_theme_item = page.get_by_role("menuitem", name="Dark")
        self.system_theme_item = page.get_by_role("menuitem", name="System")
        self.system_theme_item = page.get_by_role("menuitem", name="System")
        

    # --- Actions ---

    def navigate(self):
        self.page.goto("https://staging.admin.rhevome.com/login")
        self.page.wait_for_load_state("networkidle")

    def verify_ui_elements(self):
        """TC_01: Verify all main UI elements on the Admin Login Page"""
        expect(self.logo).to_be_visible()
        expect(self.theme_toggle_btn).to_be_visible()
        expect(self.admin_portal_header).to_be_visible()
        expect(self.portal_subtext).to_be_visible()

        # Verify Email Section
        expect(self.email_label).to_be_visible()
        expect(self.email_input).to_be_visible()

        # Verify Password Section
        expect(self.password_label).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.password_toggle_btn).to_be_visible()

        # Verify Others
        expect(self.remember_me_checkbox).to_be_visible()
        expect(self.sign_in_btn).to_be_visible()
        expect(self.hipaa_notice).to_be_visible()
        expect(self.hipaa_notice).to_be_visible()

    def login(self, email, password):
        self.email_input.click()
        self.email_input.fill(email)
        self.password_input.click()
        self.password_input.fill(password)
        self.sign_in_btn.click()

    def verify_login_error_is_displayed(self):
        expect(self.error_toast_list).to_be_visible()
        expect(self.login_failed_msg).to_be_visible()
        expect(self.invalid_credentials_msg).to_be_visible()

    def get_email_validation_message(self):
        return self.email_input.evaluate("node => node.validationMessage")

    def get_password_validation_message(self):
        return self.password_input.evaluate("node => node.validationMessage")

    def login_with_remember_me(self, email, password):
        """
        TC_06: Performs login with 'Remember Me' checkbox checked.
        """
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.remember_me_checkbox.check()
        self.sign_in_btn.click()

    def toggle_password_visibility(self):
        """
        TC_07: Clicks the eye icon to toggle password visibility.
        """
        self.password_toggle_btn.click()

    def get_password_field_type(self):
        """
        Returns the 'type' attribute of the password field (e.g., 'password' or 'text').
        """
        return self.password_input.get_attribute("type")

    def click_theme_toggle(self):
        """
        TC_08: Clicks the theme toggle button to open the theme menu.
        """
        self.theme_toggle_btn.click()

    def is_theme_menu_visible(self):
        """
        Returns True if the theme selection menu is visible.
        """
        return self.theme_menu.is_visible()
    
    def select_theme_light(self):
        """
        TC_09: Opens theme menu and selects Light mode.
        """
        self.theme_toggle_btn.click()
        self.page.wait_for_timeout(500)
        self.light_theme_item.click()

    def select_theme_dark(self):
        """
        TC_10: Opens theme menu and selects Dark mode.
        """
        self.theme_toggle_btn.click()
        self.page.wait_for_timeout(500)
        self.dark_theme_item.click()
    
    def select_theme_system(self):
        """
        TC_11: Opens theme menu and selects System mode.
        """
        self.theme_toggle_btn.click()
        self.page.wait_for_timeout(500)
        self.system_theme_item.click()
    
    
    
    

    
    

    
    
    