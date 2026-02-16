import pytest
from utils.assertions import assert_product_schema

def test_get_all_products_return_list(products_api):
    response = products_api.get_all_products()
    assert response.status_code == 200
    data = products_api.get_json(response)
    assert isinstance(data, list)
    for product in data:
        assert_product_schema(product)


@pytest.mark.parametrize("products_id", [1, 5, 20])
def test_get_product_by_id_success(products_api, products_id):
    response = products_api.get_product_by_id(products_id)
    assert response.status_code == 200
    data = products_api.get_json(response)
    assert isinstance(data, dict)
    assert_product_schema(data)
    assert data["id"] == products_id



@pytest.mark.parametrize("product_id", [0, -1, 9999])
def test_get_product_by_id_failure(products_api, product_id):
    response = products_api.get_product_by_id(product_id)
    assert response.status_code == 200
    assert response.text == ""
    assert response.content == b""
    
