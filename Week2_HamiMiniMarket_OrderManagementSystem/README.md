
# HamiMiniMarket - CLI Order Management System

This project is a Week 2 task for the HamiSkills Python Development Track.
It implements a CLI-based order management system with the following features:

- Load product inventory from `products.json`
- Display products (Somali names included)
- Add products to cart with input validation
- Calculate subtotal, apply 5% tax
- Optional 10% discount for orders over $20
- Simple staff login system (users in `users.json`) — when staff logs in, stock is reduced on checkout
- Generate receipt saved to `receipts/` with timestamp
- Modular structure: `main.py`, `inventory.py`, `order.py`

## How to run

1. Make sure you have Python 3.7+ installed.
2. Open a terminal in the project folder.
3. Run:
```
python main.py
```

Follow the on-screen prompts to login, view products, add to cart, and checkout.

## Files
- `main.py` - program entry and CLI
- `inventory.py` - inventory management (load/save/display)
- `order.py` - cart, checkout, receipt generation
- `products.json` - sample inventory with Somali product names
- `users.json` - sample staff accounts
- `receipts/` - generated receipts are stored here
