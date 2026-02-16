from requests.exceptions import JSONDecodeError
import requests
from utils.config import TIMEOUT

class BaseAPI:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, headers: dict | None = None):
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        full_url = self.base_url + endpoint
        return self.session.get(full_url, headers=headers, timeout=TIMEOUT)
    
    def post(self, endpoint: str, data: dict, headers: dict | None = None):
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        full_url = self.base_url + endpoint
        return self.session.post(full_url, headers=headers, json=data, timeout=TIMEOUT)    

    def get_json_safe(self, response) -> dict | None:
        try:
            return response.json()
        except JSONDecodeError:
            return None
