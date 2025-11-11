from inventory import Inventory
from order import Order
import getpass

TAX_RATE = 0.05
DISCOUNT_THRESHOLD = 20.0
DISCOUNT_RATE = 0.10

def login(users_file="users.json"):
    import json
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        users = []

    print("=== Hami MiniMarket Staff Login ===")
    username = input("Username: ").strip()
    password = getpass.getpass("Password (input hidden): ").strip()
    for u in users:
        if u.get("username")==username and u.get("password")==password:
            print(f"Welcome, {username}!")
            return True
    print("Login failed. Continuing as guest (no stock modification).")
    return False

def print_menu():
    print("\n--- Menu ---")
    print("1. Show Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

def main():
    inventory = Inventory("products.json")
    staff_logged_in = login()
    order = Order(inventory, staff_logged_in)

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            inventory.display_products()
        elif choice == "2":
            try:
                product_id = int(input("Enter product ID to add: ").strip())
                qty = int(input("Enter quantity: ").strip())
                order.add_to_cart(product_id, qty)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "3":
            order.show_cart()
        elif choice == "4":
            if not order.cart:
                print("Cart is empty.")
                continue
            subtotal = order.calculate_subtotal()
            discount = 0.0
            if subtotal > DISCOUNT_THRESHOLD:
                discount = subtotal * DISCOUNT_RATE
                print(f"Discount applied: ${discount:.2f}")
            taxed = (subtotal - discount) * TAX_RATE
            total = subtotal - discount + taxed
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Tax ({TAX_RATE*100:.0f}%): ${taxed:.2f}")
            print(f"Total: ${total:.2f}")
            confirm = input("Confirm checkout? (y/n): ").strip().lower()
            if confirm == "y":
                receipt_path = order.checkout(discount=discount, tax_rate=TAX_RATE)
                print(f"Receipt saved to: {receipt_path}")
                # reload inventory after purchase if staff modified stock
                inventory.reload()
                order = Order(inventory, staff_logged_in)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
