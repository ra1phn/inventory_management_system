
# Mock inventory database
inventory = [
    {
        "id": 1,
        "barcode": "3017620422003",
        "product_name": "Nutella",
        "brands": "Ferrero",
        "categories": "Spreads, Chocolate spreads",
        "quantity": "350g",
        "ingredients_text": "Sugar, palm oil, hazelnuts, cocoa",
        "nutriscore_grade": "e",
        "image_url": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_en.400.jpg",
        "price": 650.00,
        "stock": 20
    },
    {
        "id": 2,
        "barcode": "5449000000996",
        "product_name": "Coca-Cola",
        "brands": "Coca-Cola",
        "categories": "Beverages, Sodas",
        "quantity": "500ml",
        "ingredients_text": "Carbonated water, sugar, caramel colour",
        "nutriscore_grade": "e",
        "image_url": "",
        "price": 100.00,
        "stock": 50
    },
    {
        "id": 3,
        "barcode": "7622210449283",
        "product_name": "Oreo Original",
        "brands": "Mondelez",
        "categories": "Snacks, Biscuits",
        "quantity": "154g",
        "ingredients_text": "Wheat flour, sugar, palm oil, cocoa",
        "nutriscore_grade": "e",
        "image_url": "",
        "price": 180.00,
        "stock": 30
    }
]


# Get all inventory items
def get_all_items():
    return inventory


# Get one inventory item by ID
def get_item_by_id(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item

    return None


# Add a new inventory item
def add_item(item_data):
    new_id = max(item["id"] for item in inventory) + 1 if inventory else 1

    new_item = item_data.copy()
    new_item["id"] = new_id

    inventory.append(new_item)

    return new_item


# Update an existing inventory item
def update_item(item_id, updated_data):
    item = get_item_by_id(item_id)

    if item is None:
        return None

    updated_data = updated_data.copy()
    updated_data.pop("id", None)

    item.update(updated_data)

    return item


# Delete an inventory item
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return item

    return None
