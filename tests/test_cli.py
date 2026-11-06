
from unittest.mock import patch, Mock

import cli


@patch("cli.requests.get")
def test_view_inventory(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": 1,
            "product_name": "Test Product",
            "price": 100,
            "stock": 10
        }
    ]

    mock_get.return_value = mock_response

    cli.view_inventory()


@patch("cli.requests.post")
@patch("builtins.input")
def test_add_product(mock_input, mock_post):
    mock_input.side_effect = ["Test Product", "100", "10"]

    mock_response = Mock()
    mock_response.status_code = 201
    mock_post.return_value = mock_response

    cli.add_product()


@patch("cli.requests.delete")
@patch("builtins.input")
def test_delete_product(mock_input, mock_delete):
    mock_input.return_value = "1"

    mock_response = Mock()
    mock_response.status_code = 200
    mock_delete.return_value = mock_response

    cli.delete_product()
