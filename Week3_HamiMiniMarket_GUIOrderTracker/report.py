
import csv
from pathlib import Path
from collections import defaultdict

class SalesReport:
    def __init__(self, sales_dir="sales"):
        self.sales_dir = Path(sales_dir)
        self.sales_dir.mkdir(parents=True, exist_ok=True)

    def save_order(self, order_record):
        if not order_record:
            return False
        date = order_record['timestamp'].split(" ")[0]
        summary_path = self.sales_dir / f"summary_{date}.csv"
        write_header = not summary_path.exists()
        with open(summary_path, "a", newline='', encoding='utf-8') as f:
            fieldnames = ['timestamp','customer','item_name','qty','line_total']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            for item in order_record['items']:
                writer.writerow({
                    'timestamp': order_record['timestamp'],
                    'customer': order_record['customer'],
                    'item_name': item['name'],
                    'qty': item['qty'],
                    'line_total': item['price']*item['qty']
                })
        return True

    def generate_daily_report(self, date_str):
        sales_file = self.sales_dir / f"sales_{date_str}.csv"
        if not sales_file.exists():
            return None
        totals = 0.0
        counts = defaultdict(int)
        with open(sales_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                totals += float(r.get('line_total', 0))
                counts[r.get('item_name')] += int(r.get('qty', 0))
        most_sold = None
        if counts:
            most_sold = max(counts.items(), key=lambda x: x[1])
        return {'total_sales': totals, 'most_sold': most_sold}
