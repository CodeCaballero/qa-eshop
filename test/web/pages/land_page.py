from test.web.pages.base_page import BasePage


class LandPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._button_login = page.get_by_role("link", name="Sign in", exact=True)
        self._text_name_login = page.get_by_role("heading", name="alice", exact=True)

    def click_login_page(self):
        self._button_login.click()

    def load(self):
        self.navigate_to()

    def check_username(self, username: str):
        self.should_have_text(self._text_name_login, username)
