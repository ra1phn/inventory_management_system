
import pytest
import inventory
from app import app


@pytest.fixture
def client():
    inventory.inventory.clear()
    inventory.inventory.extend([
        {
            "id": 1,
            "barcode": "123456",
            "product_name": "Test Product",
            "price": 100.00,
            "stock": 10
        }
    ])

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_inventory_item(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.json["product_name"] == "Test Product"


def test_get_missing_item(client):
    response = client.get("/inventory/999")
    assert response.status_code == 404


def test_create_inventory_item(client):
    response = client.post("/inventory", json={
        "product_name": "New Product",
        "price": 200,
        "stock": 5
    })

    assert response.status_code == 201


def test_update_inventory_item(client):
    response = client.patch("/inventory/1", json={
        "price": 150
    })

    assert response.status_code == 200
    assert response.json["price"] == 150.0


def test_delete_inventory_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200


def test_delete_missing_item(client):
    response = client.delete("/inventory/999")
    assert response.status_code == 404
