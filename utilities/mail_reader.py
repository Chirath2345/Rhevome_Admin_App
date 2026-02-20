import re
import time

from playwright.sync_api import Page


class MailReader:

    def __init__(self, email_address):
        self.BASE_URL = "https://www.mailinator.com"
        self.inbox = email_address.split("@")[0]

    def get_verify_link_mailinator(
        self, page: Page, retries: int = 15, wait_seconds: int = 4
    ) -> str:
        for attempt in range(retries):
            try:
                # Open inbox
                page.goto(f"{self.BASE_URL}/v4/public/inboxes.jsp?to={self.inbox}")

                # Wait for email list
                page.wait_for_selector(
                    "//*[@ng-repeat='email in emails']", timeout=10000
                )

                # Click latest email
                page.locator("//*[@ng-repeat='email in emails']").first.click()

                # Wait for iframe to load
                page.wait_for_selector("iframe#html_msg_body", timeout=10000)

                frame = page.frame_locator("iframe#html_msg_body")

                # Wait until URL paragraph appears inside iframe
                frame.locator("p[style*='word-break: break-all']").wait_for(
                    timeout=10000
                )

                # Get verification URL
                url = frame.locator("p[style*='word-break: break-all']").text_content()

                if url:
                    return url.strip()

            except Exception:
                time.sleep(wait_seconds)

        raise TimeoutError("Verification email not received within expected time")

    def get_invite_link_mailinator(
        self, page: Page, retries: int = 10, wait_seconds: int = 3
    ) -> str:
        """
        Poll Mailinator inbox until the latest invite email is received
        and return the invited link
        """
        for attempt in range(retries):
            try:
                # Open inbox page
                page.goto(f"{self.BASE_URL}/v4/public/inboxes.jsp?to={self.inbox}")
                page.wait_for_selector(
                    "//*[@ng-repeat='email in emails']", timeout=5000
                )

                # Click the latest email
                page.locator("//*[@ng-repeat='email in emails']").first.click()
                page.wait_for_selector("iframe#html_msg_body", timeout=5000)
                frame = page.frame_locator("iframe#html_msg_body")
                reset_link = frame.locator(
                    "a", has_text="Go to Worklenz"
                ).get_attribute("href")
                assert reset_link is not None, "Invite link not found in email"
                return reset_link
            except Exception:
                time.sleep(wait_seconds)

        raise TimeoutError("Invite email not received within expected time")
