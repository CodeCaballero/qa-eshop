import pytest

from config.settings import WEB_BASE_URL
from test.web.helpers.auth_state import ensure_user_auth_state


@pytest.fixture
def page(browser, request):
    if request.node.path.name == "test_login.py":
        context = browser.new_context(ignore_https_errors=True)
    else:
        state_path = ensure_user_auth_state(browser, "alice")
        context = browser.new_context(
            storage_state=str(state_path),
            ignore_https_errors=True,
        )

    page = context.new_page()
    page.goto(WEB_BASE_URL)
    try:
        yield page
    finally:
        context.close()
