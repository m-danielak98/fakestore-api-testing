from utils.config import PASSWORD, USERNAME

def test_login_invalid_credentials_returns_401(auth_api):
    response = auth_api.login("wrong", "wrong")
    assert response.status_code == 401
    assert response.text != ""
    data = auth_api.api.get_json_safe(response)
    if isinstance(data, dict):
        assert "token" not in data
    else:
        assert data is None
    

def test_login_success_returns_token(auth_api):
    response = auth_api.login(USERNAME, PASSWORD)
    assert 200 <= response.status_code < 300
    data = auth_api.api.get_json_safe(response)
    assert isinstance(data, dict)
    token = data.get("token")
    assert isinstance(token, str)
    assert token.strip() != ""
