from playwright.sync_api import Page, Locator, expect
from typing import Optional
import time
import random


class BasePage:
    """Base page class for Playwright page objects with common methods"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to a URL"""
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
    
    def click(self, selector: str, timeout: int = 30000):
        """Click an element by selector"""
        self.page.locator(selector).click(timeout=timeout)
    
    def fill(self, selector: str, text: str, timeout: int = 30000):
        """Fill an input field by selector"""
        self.page.locator(selector).fill(text, timeout=timeout)
    
    def type(self, selector: str, text: str, timeout: int = 30000):
        """Type text into an input field (slower, more realistic)"""
        self.page.locator(selector).type(text, timeout=timeout)
    
    def get_text(self, selector: str, timeout: int = 30000) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).inner_text(timeout=timeout)
    
    def get_attribute(self, selector: str, attribute: str, timeout: int = 30000) -> Optional[str]:
        """Get attribute value of an element"""
        return self.page.locator(selector).get_attribute(attribute, timeout=timeout)
    
    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible"""
        try:
            return self.page.locator(selector).is_visible(timeout=timeout)
        except:
            return False
    
    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for selector to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def wait_for_element(self, selector: str, state: str = "visible", timeout: int = 30000):
        """Wait for element to reach a specific state"""
        self.page.wait_for_selector(selector, state=state, timeout=timeout)
    
    def select_option(self, selector: str, value: str, timeout: int = 30000):
        """Select an option from a dropdown"""
        self.page.locator(selector).select_option(value, timeout=timeout)
    
    def press_key(self, selector: str, key: str, timeout: int = 30000):
        """Press a key on an element"""
        self.page.locator(selector).press(key, timeout=timeout)
    
    def clear_and_fill(self, selector: str, text: str, timeout: int = 30000):
        """Clear input field and fill with new text"""
        locator = self.page.locator(selector)
        locator.clear(timeout=timeout)
        locator.fill(text, timeout=timeout)
    
    def scroll_to_element(self, selector: str, timeout: int = 30000):
        """Scroll to an element"""
        self.page.locator(selector).scroll_into_view_if_needed(timeout=timeout)
    
    def get_locator(self, selector: str) -> Locator:
        """Get a locator for an element"""
        return self.page.locator(selector)
    
    def wait_for_timeout(self, milliseconds: int):
        """Wait for a specific time (use sparingly, prefer wait_for_selector)"""
        self.page.wait_for_timeout(milliseconds)
    
    def sleep(self, seconds: float):
        """Sleep for a specific time (use sparingly)"""
        time.sleep(seconds)
    
    def execute_script(self, script: str):
        """Execute JavaScript"""
        self.page.evaluate(script)
    
    def take_screenshot(self, path: str):
        """Take a screenshot"""
        self.page.screenshot(path=path)

    def random_color_select(self):
        """Select a random color from the color palette"""
        palette = self.page.locator("//div[@class='ant-color-picker-palette']")
        palette.wait_for()
        # get bounding box of the palette
        box = palette.bounding_box()

        # generate random x,y inside the palette
        random_x = box["x"] + random.uniform(5, box["width"] - 5)
        random_y = box["y"] + random.uniform(5, box["height"] - 5)

        # click the random point
        self.page.mouse.click(random_x, random_y)


