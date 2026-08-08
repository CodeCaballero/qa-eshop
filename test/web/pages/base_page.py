from playwright.sync_api import Page, Locator, expect

from config.settings import WEB_BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self):
        self.page.goto(WEB_BASE_URL)

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, text: str):
        locator.fill(text)

    def should_be_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def should_have_text(self, locator: Locator, text: str):
        expect(locator).to_contain_text(text)
