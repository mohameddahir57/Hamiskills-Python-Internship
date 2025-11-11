
import json
from pathlib import Path

class Inventory:
    def __init__(self, filepath="products.json"):
        self.filepath = Path(filepath)
        self._load()

    def _load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.products = json.load(f)
        except Exception:
            self.products = []

    def reload(self):
        self._load()

    def save(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.products, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("Error saving inventory:", e)

    def display_products(self):
        print("\nAvailable Products:")
        print(f"{'ID':<4}{'Name':<25}{'Price':<10}{'Stock':<8}")
        for p in self.products:
            print(f"{p['id']:<4}{p['name']:<25}{p['price']:<10.2f}{p['stock']:<8}")

    def get_product(self, product_id):
        for p in self.products:
            if p['id'] == product_id:
                return p
        return None

    def reduce_stock(self, product_id, qty):
        p = self.get_product(product_id)
        if p is None:
            return False, "Product not found."
        if p['stock'] < qty:
            return False, f"Not enough stock. Available: {p['stock']}"
        p['stock'] -= qty
        self.save()
        return True, None
