import pytest
from config.settings import API_BASE_URL
from config.users import get_password_user
from test.api.helpers.api_client import ApiClient


@pytest.fixture
def api_client(playwright):
    base_url = API_BASE_URL
    api_context = playwright.request.new_context(base_url=base_url)
    yield ApiClient(api_context, base_url=base_url)
    api_context.dispose()

