
import requests


BASE_URL = "https://world.openfoodfacts.org"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0"
}


def format_product(product):
    """Return product details in the format used by our inventory."""

    return {
        "barcode": product.get("code", ""),
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "categories": product.get("categories", ""),
        "quantity": product.get("quantity", ""),
        "ingredients_text": product.get("ingredients_text", ""),
        "nutriscore_grade": product.get("nutriscore_grade", ""),
        "image_url": product.get("image_front_url", "")
    }


def get_product_by_barcode(barcode):
    """Find a product using its barcode."""

    url = f"{BASE_URL}/api/v2/product/{barcode}.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        if data.get("status") == 1:
            return format_product(data.get("product", {}))

        return None

    except requests.RequestException as error:
        print(f"Error connecting to OpenFoodFacts: {error}")
        return None


def search_product_by_name(product_name):
    """Search for a product using its name."""

    url = f"{BASE_URL}/cgi/search.pl"

    parameters = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 1,
        "fields": "code,product_name,brands,categories,quantity,"
                  "ingredients_text,nutriscore_grade,image_front_url"
    }

    try:
        response = requests.get(
            url,
            params=parameters,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        products = data.get("products", [])

        if products:
            return format_product(products[0])

        return None

    except requests.RequestException as error:
        print(f"Error connecting to OpenFoodFacts: {error}")
        return None
