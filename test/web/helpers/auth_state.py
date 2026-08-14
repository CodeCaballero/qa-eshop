from config.paths import AUTH_DIR
from playwright.sync_api import Browser, expect

from config.users import get_password_user
from test.web.pages.land_page import LandPage
from test.web.pages.login_page import LoginPage


def login_user(page, username: str, password: str) -> None:
    land = LandPage(page)
    login = LoginPage(page)
    land.click_login_page()
    login.do_login(username, password)
    login.click_login()
    expect(land.check_login_success(username)).to_be_visible()


def ensure_user_auth_state(browser: Browser, username: str) -> str:
    AUTH_DIR.mkdir(parents=True, exist_ok=True)
    state_path = AUTH_DIR / f"{username.lower()}.json"

    if not state_path.exists():
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        login_user(page, username, get_password_user(username))
        context.storage_state(path=state_path)
        context.close()

    return str(state_path)
