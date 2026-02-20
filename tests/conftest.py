import datetime
import os
import sys
from pathlib import Path

import pytest
from playwright.sync_api import Page, sync_playwright

# --- PATH FIX START ---
root_path = str(Path(__file__).parent.parent)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
# --- PATH FIX END ---

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)


@pytest.fixture(scope="function")
def page():
    """Playwright page fixture"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def authenticated_page(page):
    """Page fixture with user already logged in"""

    from pages.login_page import LoginPage
    from utilities.config_reader import ConfigReader

    config = ConfigReader()
    login_page = LoginPage(page)
    login_page.navigate(config.get_application_url())
    # login_page.accept_cookies_if_present()

    email = config.get_email()
    password = config.get_password()
    login_page.enter_credentials(email, password)

    # Wait for login to complete
    page.wait_for_timeout(3000)

    yield page


# Hook to capture screenshot on failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/{item.name}_{timestamp}.png"
            try:
                page.screenshot(path=screenshot_path)
                print(f"📸 Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"⚠️ Could not capture screenshot: {e}")
