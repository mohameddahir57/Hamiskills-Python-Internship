"""
Hami MiniMarket - Week 1 Task
Product Inventory System (Command-line)

Features:
- Add a new product (name, category, price, quantity)
- View all products in a formatted table
- Update stock quantity of an existing product
- Calculate the total value of all products in stock
- Save / Load data to JSON (data.json)
- Search product by name (case-insensitive)

Run:
    python main.py

Author: Generated for internship submission
"""

import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_data(filename=DATA_FILE):
    """Load product list from JSON file. Returns a list of products (dicts)."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except Exception as e:
        print(f"Warning: failed to load {filename}: {e}")
        return []

def save_data(products, filename=DATA_FILE):
    """Save product list (list of dicts) to JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data: {e}")

def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty. Please try again.")

def input_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except:
            print("Invalid number. Please enter a numeric value (e.g., 3.50).")

def input_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            value = int(s)
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except:
            print("Invalid integer. Please enter a whole number (e.g., 5).")

def add_product(products):
    print("\nAdd New Product")
    name = input_nonempty("Name: ")
    category = input_nonempty("Category: ")
    price = input_float("Price (e.g., 2.50): ")
    quantity = input_int("Quantity (integer): ")
    # Check for existing product with same name (case-insensitive)
    for p in products:
        if p.get("name","").lower() == name.lower():
            print("Product with this name already exists. Use option to update quantity instead.")
            return
    product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "added": datetime.utcnow().isoformat() + "Z"
    }
    products.append(product)
    save_data(products)
    print(f"Product '{name}' added.\n")

def view_products(products):
    print("\nAll Products\n")
    if not products:
        print("No products found.\n")
        return
    # Determine column widths
    headers = ["ID", "Name", "Category", "Price", "Quantity", "Value"]
    rows = []
    for i, p in enumerate(products, start=1):
        try:
            value = p.get("price",0) * p.get("quantity",0)
        except:
            value = 0
        rows.append([i, p.get("name",""), p.get("category",""), f"{p.get('price',0):.2f}", p.get("quantity",0), f"{value:.2f}"])
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]
    # Print header
    header_line = " | ".join(h.ljust(col_widths[i]) for i,h in enumerate(headers))
    sep_line = "-+-".join("-"*col_widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep_line)
    for r in rows:
        print(" | ".join(str(r[i]).ljust(col_widths[i]) for i in range(len(r))))
    print("")

def find_product_by_name(products, name):
    name_lower = name.strip().lower()
    matches = []
    for i, p in enumerate(products, start=1):
        if name_lower in p.get("name","").lower():
            matches.append((i,p))
    return matches

def update_quantity(products):
    print("\nUpdate Quantity")
    name = input_nonempty("Enter product name or partial name: ")
    matches = find_product_by_name(products, name)
    if not matches:
        print("No product matched that name.\n")
        return
    print(f"Found {len(matches)} match(es):")
    for idx, (i,p) in enumerate(matches, start=1):
        print(f"{idx}. {p.get('name')} (Category: {p.get('category')}) - Current quantity: {p.get('quantity')}")
    choice = input_int("Select item number to update (0 to cancel): ")
    if choice == 0:
        print("Cancelled.\n")
        return
    if choice < 1 or choice > len(matches):
        print("Invalid selection.\n")
        return
    selected = matches[choice-1][1]
    print(f"Selected: {selected.get('name')} — current quantity: {selected.get('quantity')}")
    new_qty = input_int("Enter new quantity (integer): ")
    selected['quantity'] = new_qty
    save_data(products)
    print(f"Quantity updated for '{selected.get('name')}'.\n")

def calculate_total_value(products):
    total = 0.0
    for p in products:
        try:
            total += float(p.get("price",0)) * int(p.get("quantity",0))
        except:
            continue
    print(f"\nTotal inventory value: {total:.2f}\n")
    return total

def search_products(products):
    print("\nSearch Products")
    term = input_nonempty("Search term (name): ")
    matches = find_product_by_name(products, term)
    if not matches:
        print("No products matched your search.\n")
        return
    print(f"Found {len(matches)} match(es):\n")
    for i,p in matches:
        print(f"- {p.get('name')} (Category: {p.get('category')}), Price: {p.get('price'):.2f}, Quantity: {p.get('quantity')}")
    print("")

def delete_product(products):
    print("\nDelete Product")
    name = input_nonempty("Enter product name or partial name to delete: ")
    matches = find_product_by_name(products, name)
    if not matches:
        print("No product matched that name.\n")
        return
    print(f"Found {len(matches)} match(es):")
    for idx, (i,p) in enumerate(matches, start=1):
        print(f"{idx}. {p.get('name')} - Quantity: {p.get('quantity')}")
    choice = input_int("Select item number to delete (0 to cancel): ")
    if choice == 0:
        print("Cancelled.\n")
        return
    if choice < 1 or choice > len(matches):
        print("Invalid selection.\n")
        return
    # Remove the selected product from the main list
    # matches contain indices relative to original list
    real_index = matches[choice-1][0] - 1
    removed = products.pop(real_index)
    save_data(products)
    print(f"Removed product '{removed.get('name')}'.\n")

def clear_all(products):
    print("\nClear All Products")
    confirm = input("Type 'YES' to permanently delete all products: ")
    if confirm == "YES":
        products.clear()
        save_data(products)
        print("All products removed.\n")
    else:
        print("Cancelled.\n")

def show_menu():
    print("Hami MiniMarket — Inventory System")
    print("1. Add new product")
    print("2. View all products")
    print("3. Update quantity")
    print("4. Calculate total inventory value")
    print("5. Search products")
    print("6. Delete product (optional)")
    print("7. Clear all products (dangerous)")
    print("0. Exit")

def main():
    products = load_data()
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            add_product(products)
        elif choice == "2":
            view_products(products)
        elif choice == "3":
            update_quantity(products)
        elif choice == "4":
            calculate_total_value(products)
        elif choice == "5":
            search_products(products)
        elif choice == "6":
            delete_product(products)
        elif choice == "7":
            clear_all(products)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from the menu.\n")

if __name__ == "__main__":
    main()