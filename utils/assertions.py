def assert_product_schema(product: dict):
    keys = ["id", "title", "price", "description", "category", "image", "rating"]
    assert isinstance(product, dict)
    for key in keys:
        assert key in product, f"Missing key: {key}"
    
    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["description"], str)
    assert isinstance(product["category"], str)
    assert isinstance(product["image"], str)

    rating = product["rating"]
    assert isinstance(rating, dict)
    assert "rate" in rating
    assert "count" in rating
    assert isinstance(rating["rate"], (int, float))
    assert isinstance(rating["count"], int)
    