
import csv
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

class Inventory:
    def __init__(self, csv_path="inventory.csv"):
        self.csv_path = Path(csv_path)
        self.products = []
        self._load()

    def _load(self):
        self.products = []
        if not self.csv_path.exists():
            return
        with open(self.csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                try:
                    p = Product(int(r['id']), r['name'], float(r['price']), int(r['stock']))
                    self.products.append(asdict(p))
                except Exception:
                    continue

    def save(self):
        with open(self.csv_path, "w", newline='', encoding='utf-8') as f:
            fieldnames = ['id','name','price','stock']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.products:
                writer.writerow({'id':p['id'],'name':p['name'],'price':p['price'],'stock':p['stock']})

    def get_product(self, product_id):
        for p in self.products:
            if p['id'] == product_id:
                return p
        return None

    def reduce_stock(self, product_id, qty):
        p = self.get_product(product_id)
        if not p:
            return False, "Product not found."
        if p['stock'] < qty:
            return False, f"Not enough stock. Available: {p['stock']}"
        p['stock'] -= qty
        self.save()
        return True, None

    def restock_from_csv(self, restock_path="restock.csv"):
        added = 0
        pth = Path(restock_path)
        if not pth.exists():
            return added
        with open(pth, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                try:
                    pid = int(r['id'])
                    add = int(r['additional_stock'])
                except Exception:
                    continue
                prod = self.get_product(pid)
                if prod:
                    prod['stock'] += add
                    added += 1
        self.save()
        return added
