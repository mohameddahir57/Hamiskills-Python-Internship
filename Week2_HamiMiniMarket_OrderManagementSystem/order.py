
import os
from datetime import datetime

class Order:
    def __init__(self, inventory, staff_logged_in=False):
        self.inventory = inventory
        self.cart = []
        self.staff_logged_in = staff_logged_in
        self.receipts_dir = os.path.join(os.path.dirname(__file__), "receipts")
        os.makedirs(self.receipts_dir, exist_ok=True)

    def add_to_cart(self, product_id, qty):
        p = self.inventory.get_product(product_id)
        if not p:
            print("Product not found.")
            return
        if qty <= 0:
            print("Quantity must be at least 1.")
            return
        if p['stock'] < qty:
            print(f"Insufficient stock. Available: {p['stock']}")
            return
        # Add to cart (do not reduce stock until checkout unless staff)
        self.cart.append({"id": p['id'], "name": p['name'], "price": p['price'], "qty": qty})
        print(f"Added {qty} x {p['name']} to cart.")

    def show_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("\nCart:")
        print(f"{'Name':<25}{'Qty':<6}{'Price':<10}{'Total':<10}")
        for item in self.cart:
            total = item['price'] * item['qty']
            print(f"{item['name']:<25}{item['qty']:<6}{item['price']:<10.2f}{total:<10.2f}")

    def calculate_subtotal(self):
        return sum(item['price'] * item['qty'] for item in self.cart)

    def checkout(self, discount=0.0, tax_rate=0.05):
        # Reduce stock if staff is logged in
        if self.staff_logged_in:
            for item in self.cart:
                success, msg = self.inventory.reduce_stock(item['id'], item['qty'])
                if not success:
                    print("Error during stock reduction:", msg)
        # Prepare receipt
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"receipt_{timestamp}.txt"
        path = os.path.join(self.receipts_dir, filename)
        subtotal = self.calculate_subtotal()
        taxed = (subtotal - discount) * tax_rate
        total = subtotal - discount + taxed
        with open(path, "w", encoding="utf-8") as f:
            f.write("Hami MiniMarket - Receipt\n")
            f.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"{'Name':<25}{'Qty':<6}{'Price':<10}{'Total':<10}\n")
            for item in self.cart:
                total_line = item['price'] * item['qty']
                f.write(f"{item['name']:<25}{item['qty']:<6}{item['price']:<10.2f}{total_line:<10.2f}\n")
            f.write("\n")
            f.write(f"Subtotal: ${subtotal:.2f}\n")
            if discount > 0:
                f.write(f"Discount: -${discount:.2f}\n")
            f.write(f"Tax ({tax_rate*100:.0f}%): ${taxed:.2f}\n")
            f.write(f"Total: ${total:.2f}\n")
        # clear cart after checkout
        self.cart = []
        return path
