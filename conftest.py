import pytest
from utils.config import BASE_URL, PASSWORD, USERNAME
from api.base_api import BaseAPI
from api.products_api import ProductsAPI
from api.auth_api import AuthAPI

@pytest.fixture
def products_api():
    base_api = BaseAPI(BASE_URL)
    products_api = ProductsAPI(base_api)
    return products_api

@pytest.fixture
def auth_api():
    base_api = BaseAPI(BASE_URL)
    auth_api = AuthAPI(base_api)
    return auth_api

@pytest.fixture(scope="session")
def auth_token() -> str:
    base_api = BaseAPI(BASE_URL)
    auth_api = AuthAPI(base_api)

    response = auth_api.login(USERNAME, PASSWORD)
    assert 200 <= response.status_code < 300
    data = base_api.get_json_safe(response)
    assert isinstance(data, dict), f"Login response is not JSON. Body: {response.text}"
    token = data.get("token")
    assert isinstance(token, str) and token.strip() != ""
    return token