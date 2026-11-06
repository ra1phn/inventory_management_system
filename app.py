
from flask import Flask, jsonify, request

from inventory import (
    get_all_items,
    get_item_by_id,
    add_item,
    update_item,
    delete_item
)

app = Flask(__name__)


# GET /inventory
# Fetch all inventory items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    items = get_all_items()

    return jsonify(items), 200


# GET /inventory/<id>
# Fetch one inventory item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = get_item_by_id(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


# POST /inventory
# Add a new inventory item
@app.route("/inventory", methods=["POST"])
def create_inventory_item():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    if "product_name" not in data or "price" not in data or "stock" not in data:
        return jsonify({
            "error": "Product name, price and stock are required"
        }), 400

    if not isinstance(data["product_name"], str) or not data["product_name"].strip():
        return jsonify({"error": "Product name must be a non-empty string"}), 400

    try:
        price = float(data["price"])
        stock = int(data["stock"])

        if price < 0 or stock < 0:
            return jsonify({"error": "Price and stock cannot be negative"}), 400

    except (ValueError, TypeError):
        return jsonify({"error": "Price and stock must be valid numbers"}), 400

    data["price"] = price
    data["stock"] = stock

    new_item = add_item(data)

    return jsonify(new_item), 201


# PATCH /inventory/<id>
# Update an existing inventory item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Valid update data is required"}), 400

    allowed_fields = [
        "barcode",
        "product_name",
        "brands",
        "categories",
        "quantity",
        "ingredients_text",
        "nutriscore_grade",
        "image_url",
        "price",
        "stock"
    ]

    for key in data:
        if key not in allowed_fields:
            return jsonify({"error": f"Invalid field: {key}"}), 400

    if "product_name" in data:
        if not isinstance(data["product_name"], str) or not data["product_name"].strip():
            return jsonify({"error": "Product name must be a non-empty string"}), 400

    try:
        if "price" in data:
            data["price"] = float(data["price"])

            if data["price"] < 0:
                return jsonify({"error": "Price cannot be negative"}), 400

        if "stock" in data:
            data["stock"] = int(data["stock"])

            if data["stock"] < 0:
                return jsonify({"error": "Stock cannot be negative"}), 400

    except (ValueError, TypeError):
        return jsonify({"error": "Price and stock must be valid numbers"}), 400

    updated_item = update_item(item_id, data)

    if updated_item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(updated_item), 200


# DELETE /inventory/<id>
# Delete an inventory item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_inventory_item(item_id):
    deleted_item = delete_item(item_id)

    if deleted_item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({
        "message": "Item deleted successfully",
        "item": deleted_item
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
