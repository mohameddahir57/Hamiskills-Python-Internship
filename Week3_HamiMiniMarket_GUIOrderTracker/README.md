
# Week3_HamiMiniMarket_GUIOrderTracker

This project is Week 3 task for the HamiSkills Python Development Track.
It implements a Tkinter-based GUI application for inventory and order tracking.

## Structure
- `gui.py` - Tkinter application (GUI entry)
- `inventory.py` - Product dataclass and Inventory class (CSV load/save/restock)
- `order.py` - Order class (cart management, checkout, writes sales CSV)
- `report.py` - SalesReport class (summary files and daily report)
- `inventory.csv` - sample product inventory (Somali names included)
- `restock.csv` - sample restock CSV
- `sales/` - folder where daily sales and summaries are saved

## How to run
1. Ensure Python 3.7+ is installed.
2. From the project folder run:
```
python gui.py
```
3. Use the GUI to add products to cart, confirm orders, and restock.

## Notes
- Orders are saved in `sales/sales_YYYY-MM-DD.csv` with timestamp and customer name.
- Low stock items are visible by stock number (below 5 is considered low).
- The project uses simple CSV files to simulate data persistence and is ready to upload to GitHub.
