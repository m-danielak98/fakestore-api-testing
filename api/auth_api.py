from api.base_api import BaseAPI

class AuthAPI:
    def __init__(self, api: BaseAPI):
        self.api = api

    def login(self, username: str, password: str):
        payload = {"username": username, "password": password}
        response = self.api.post("/auth/login", payload)
        return response
