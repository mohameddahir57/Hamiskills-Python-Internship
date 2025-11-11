
import csv
from datetime import datetime
from pathlib import Path

class Order:
    def __init__(self, inventory):
        self.inventory = inventory
        self.cart = []
        self.last_order_record = None

    def add_to_cart(self, product_id, qty):
        p = self.inventory.get_product(product_id)
        if not p:
            return False, "Product not found."
        if qty <= 0:
            return False, "Quantity must be at least 1."
        if p['stock'] < qty:
            return False, f"Insufficient stock. Available: {p['stock']}"
        for item in self.cart:
            if item['id'] == product_id:
                item['qty'] += qty
                return True, None
        self.cart.append({'id':p['id'],'name':p['name'],'price':float(p['price']),'qty':qty})
        return True, None

    def calculate_subtotal(self):
        return sum(item['price'] * item['qty'] for item in self.cart)

    def checkout(self, customer_name=None):
        # reduce stock
        for item in self.cart:
            self.inventory.reduce_stock(item['id'], item['qty'])
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        filename = f"sales_{date_str}.csv"
        sales_dir = Path("sales")
        sales_dir.mkdir(parents=True, exist_ok=True)
        filepath = sales_dir / filename
        write_header = not filepath.exists()
        with open(filepath, "a", newline='', encoding='utf-8') as f:
            fieldnames = ['timestamp','customer','item_id','item_name','qty','price','line_total']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            for item in self.cart:
                writer.writerow({
                    'timestamp': now.strftime("%Y-%m-%d %H:%M:%S"),
                    'customer': customer_name or "",
                    'item_id': item['id'],
                    'item_name': item['name'],
                    'qty': item['qty'],
                    'price': item['price'],
                    'line_total': item['price']*item['qty']
                })
        self.last_order_record = {
            'timestamp': now.strftime("%Y-%m-%d %H:%M:%S"),
            'customer': customer_name or "",
            'items': list(self.cart),
            'subtotal': self.calculate_subtotal()
        }
        return True

    def clear_cart(self):
        self.cart = []
