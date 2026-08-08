from config.settings import API_BASE_URL


class ApiClient:
    def __init__(self, request, base_url: str | None = None):
        if base_url is None:
            base_url = API_BASE_URL
        self.request = request
        self.base_url = base_url.rstrip("/")

