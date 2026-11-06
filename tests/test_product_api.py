
from unittest.mock import Mock, patch

from product_api import (
    get_product_by_barcode,
    search_product_by_name
)


@patch("product_api.requests.get")
def test_get_product_by_barcode(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": 1,
        "product": {
            "code": "123456",
            "product_name": "Test Product",
            "brands": "Test Brand"
        }
    }

    mock_get.return_value = mock_response

    product = get_product_by_barcode("123456")

    assert product["product_name"] == "Test Product"
    assert product["barcode"] == "123456"


@patch("product_api.requests.get")
def test_search_product_by_name(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "products": [
            {
                "code": "123456",
                "product_name": "Test Product",
                "brands": "Test Brand"
            }
        ]
    }

    mock_get.return_value = mock_response

    product = search_product_by_name("Test Product")

    assert product["product_name"] == "Test Product"


@patch("product_api.requests.get")
def test_product_not_found(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "status": 0,
        "product": {}
    }

    mock_get.return_value = mock_response

    product = get_product_by_barcode("000000")

    assert product is None
