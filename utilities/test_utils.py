import time
from playwright.sync_api import Page
from typing import Optional


def sleep(seconds: float = 1.0):
    """Sleep for specified seconds"""
    time.sleep(seconds)


def sleep3(seconds: float = 3.0):
    """Sleep for 3 seconds (or specified)"""
    time.sleep(seconds)


def sleep5(seconds: float = 5.0):
    """Sleep for 5 seconds (or specified)"""
    time.sleep(seconds)


def wait_for_page_load(page: Page, timeout: int = 30000):
    """Wait for page to load completely"""
    page.wait_for_load_state("networkidle", timeout=timeout)


def wait_for_dom_ready(page: Page, timeout: int = 30000):
    """Wait for DOM to be ready"""
    page.wait_for_load_state("domcontentloaded", timeout=timeout)


def get_element_count(page: Page, selector: str) -> int:
    """Get count of elements matching selector"""
    return page.locator(selector).count()


def is_element_present(page: Page, selector: str, timeout: int = 5000) -> bool:
    """Check if element is present on page"""
    try:
        return page.locator(selector).count() > 0
    except:
        return False


def wait_for_element_count(page: Page, selector: str, expected_count: int, timeout: int = 30000):
    """Wait for element count to match expected count"""
    start_time = time.time()
    while time.time() - start_time < timeout / 1000:
        count = page.locator(selector).count()
        if count == expected_count:
            return True
        time.sleep(0.5)
    return False

