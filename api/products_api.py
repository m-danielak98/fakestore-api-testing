from api.base_api import BaseAPI

class ProductsAPI:

    def __init__(self, api: BaseAPI):
        self.api = api

    def get_all_products(self):
        return self.api.get("/products")
    
    def get_product_by_id(self, product_id: int):
        return self.api.get(f"/products/{product_id}")

    def get_json(self, response):
        return self.api.get_json_safe(response)
