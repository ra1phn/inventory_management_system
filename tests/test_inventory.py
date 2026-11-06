
import inventory


def setup_function():
    inventory.inventory.clear()
    inventory.inventory.extend([
        {
            "id": 1,
            "product_name": "Test Product",
            "price": 100.00,
            "stock": 10
        }
    ])


def test_get_all_items():
    items = inventory.get_all_items()
    assert len(items) == 1


def test_get_item_by_id():
    item = inventory.get_item_by_id(1)
    assert item["product_name"] == "Test Product"


def test_add_item():
    item = inventory.add_item({
        "product_name": "New Product",
        "price": 200.00,
        "stock": 5
    })

    assert item["id"] == 2
    assert item["product_name"] == "New Product"


def test_update_item():
    item = inventory.update_item(1, {"price": 150.00})
    assert item["price"] == 150.00


def test_delete_item():
    item = inventory.delete_item(1)
    assert item["product_name"] == "Test Product"
    assert inventory.get_item_by_id(1) is None
