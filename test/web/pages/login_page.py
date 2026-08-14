
class LoginPage:
    def __init__(self,page):
        self.page = page
        self._input_user = page.get_by_role("textbox", name="Username")
        self._input_pass = page.get_by_placeholder("Password")
        self._btn_submit = page.get_by_role("button", name="Login")
        self._text_error_login = page.get_by_role("listitem", name="Invalid username or password", exact=True)

    def do_login(self, username: str, password: str):
        self._input_user.fill(username)
        self._input_pass.fill(password)

    def click_login(self):
        self._btn_submit.click()
