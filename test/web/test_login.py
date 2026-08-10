from config.users import get_password_user
from test.web.helpers.auth_state import ensure_user_auth_state, login_user
from test.web.pages.land_page import LandPage
from test.web.pages.login_page import LoginPage


def test_successful_login_with_valid_credentials(page):
    for i in range(1, 10):
        login_user(page, "alice", get_password_user("alice"))


def test_login_storage_state(browser):
    state_path = ensure_user_auth_state(browser, "alice")
    context = browser.new_context(
        storage_state=str(state_path),
        ignore_https_errors=True,
    )
    page = context.new_page()

    try:
        land = LandPage(page)
        land.load()
        land.check_username("alice")
    finally:
        context.close()
