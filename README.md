
# Inventory Management System

A beginner-friendly inventory management application built with Python and Flask.

The system allows users to manage products, update prices and stock quantities, and search for product information using the OpenFoodFacts API.

## Features

- View all inventory products.
- View an individual product.
- Add new products.
- Update product prices and stock.
- Delete products.
- Search for products using barcodes.
- Search for products using product names.
- Add products retrieved from OpenFoodFacts to inventory.
- Command-line interface for inventory management.
- Automated tests using pytest.

## Technologies Used

- Python
- Flask
- Requests
- OpenFoodFacts API
- Pytest
- Postman

## Project Structure

```text
inventory_management_system/
│
├── app.py
├── cli.py
├── inventory.py
├── product_api.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    ├── test_app.py
    ├── test_cli.py
    ├── test_inventory.py
    └── test_product_api.py
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd inventory_management_system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Linux and macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask API:

```bash
python app.py
```

The API runs at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/inventory` | View all products |
| GET | `/inventory/<id>` | View one product |
| POST | `/inventory` | Add a product |
| PATCH | `/inventory/<id>` | Update a product |
| DELETE | `/inventory/<id>` | Delete a product |

### Adding a Product

Send a POST request to:

```text
http://127.0.0.1:5000/inventory
```

Example JSON:

```json
{
    "product_name": "Milk",
    "price": 120,
    "stock": 20
}
```

### Updating a Product

Send a PATCH request to:

```text
http://127.0.0.1:5000/inventory/1
```

Example JSON:

```json
{
    "price": 150
}
```

### Deleting a Product

Send a DELETE request to:

```text
http://127.0.0.1:5000/inventory/1
```

## Command-Line Interface

Keep the Flask server running in one terminal.

Open a second terminal, activate the virtual environment, and run:

```bash
python cli.py
```

The CLI provides options to:

1. View inventory.
2. Add products.
3. Update products.
4. Delete products.
5. Search for products using OpenFoodFacts.
6. Exit.

## OpenFoodFacts Integration

The application uses the OpenFoodFacts API to retrieve product information.

Products can be searched using:

- Product barcodes.
- Product names.

Retrieved product information can be added to the local inventory.

## Running Tests

Run the automated test suite using:

```bash
pytest -v
```

## Important Note

The current inventory is stored in a Python list in memory. This means inventory changes are reset when the Flask application restarts.

The application is intended as a learning project demonstrating Flask API development, CRUD operations, external API integration, command-line interfaces and automated testing.

## Author

Inventory Management System Project
