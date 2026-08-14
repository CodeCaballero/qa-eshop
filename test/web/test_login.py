from playwright.sync_api import expect

from config.users import get_password_user
from test.web.helpers.auth_state import login_user


def test_successful_login_with_valid_credentials(page):
    login_user(page,"alice", get_password_user("alice"))

