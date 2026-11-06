
import requests

from product_api import get_product_by_barcode, search_product_by_name


API_URL = "http://127.0.0.1:5000/inventory"


def view_inventory():
    try:
        response = requests.get(API_URL, timeout=5)

        if response.status_code == 200:
            items = response.json()

            print("\n--- INVENTORY ---")

            for item in items:
                print(
                    f"ID: {item['id']} | "
                    f"Name: {item['product_name']} | "
                    f"Price: {item['price']} | "
                    f"Stock: {item['stock']}"
                )
        else:
            print("Could not retrieve inventory.")

    except requests.RequestException:
        print("Could not connect to the inventory API.")


def add_product():
    product_name = input("Enter product name: ")
    price = input("Enter product price: ")
    stock = input("Enter stock quantity: ")

    try:
        data = {
            "product_name": product_name,
            "price": float(price),
            "stock": int(stock)
        }

        response = requests.post(API_URL, json=data, timeout=5)

        if response.status_code == 201:
            print("Product added successfully.")
        else:
            print("Could not add product:", response.json())

    except ValueError:
        print("Price and stock must be valid numbers.")
    except requests.RequestException:
        print("Could not connect to the inventory API.")


def update_product():
    try:
        item_id = int(input("Enter product ID: "))

        print("1. Update price")
        print("2. Update stock")

        choice = input("Choose an option: ")

        if choice == "1":
            value = float(input("Enter new price: "))
            data = {"price": value}
        elif choice == "2":
            value = int(input("Enter new stock: "))
            data = {"stock": value}
        else:
            print("Invalid option.")
            return

        response = requests.patch(
            f"{API_URL}/{item_id}",
            json=data,
            timeout=5
        )

        if response.status_code == 200:
            print("Product updated successfully.")
        else:
            print("Could not update product:", response.json())

    except ValueError:
        print("Please enter valid numbers.")
    except requests.RequestException:
        print("Could not connect to the inventory API.")


def delete_product():
    try:
        item_id = int(input("Enter product ID: "))

        response = requests.delete(
            f"{API_URL}/{item_id}",
            timeout=5
        )

        if response.status_code == 200:
            print("Product deleted successfully.")
        else:
            print("Could not delete product:", response.json())

    except ValueError:
        print("Please enter a valid product ID.")
    except requests.RequestException:
        print("Could not connect to the inventory API.")


def find_product():
    print("\n1. Search by barcode")
    print("2. Search by product name")

    choice = input("Choose an option: ")

    if choice == "1":
        barcode = input("Enter product barcode: ")
        product = get_product_by_barcode(barcode)
    elif choice == "2":
        name = input("Enter product name: ")
        product = search_product_by_name(name)
    else:
        print("Invalid option.")
        return

    if product:
        print("\n--- PRODUCT FOUND ---")
        for key, value in product.items():
            print(f"{key}: {value}")

        add_choice = input("\nAdd this product to inventory? (yes/no): ")

        if add_choice.lower() == "yes":
            try:
                price = float(input("Enter selling price: "))
                stock = int(input("Enter stock quantity: "))

                product["price"] = price
                product["stock"] = stock

                response = requests.post(
                    API_URL,
                    json=product,
                    timeout=5
                )

                if response.status_code == 201:
                    print("Product added successfully.")
                else:
                    print("Could not add product:", response.json())

            except ValueError:
                print("Please enter valid price and stock numbers.")
            except requests.RequestException:
                print("Could not connect to the inventory API.")

    else:
        print("Product not found.")


def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. View inventory")
        print("2. Add product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Find product using OpenFoodFacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            find_product()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
