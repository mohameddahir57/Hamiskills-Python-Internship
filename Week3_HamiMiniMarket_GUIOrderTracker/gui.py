
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from inventory import Inventory
from order import Order
from report import SalesReport
from datetime import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hami MiniMarket - GUI Order Tracker")
        self.geometry("900x520")

        self.inventory = Inventory("inventory.csv")
        self.order = Order(self.inventory)
        self.report = SalesReport("sales")

        self.create_widgets()
        self.refresh_products()

    def create_widgets(self):
        products_frame = ttk.LabelFrame(self, text="Products")
        products_frame.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        cols = ("ID","Name","Price","Stock")
        self.tree = ttk.Treeview(products_frame, columns=cols, show="headings", height=18)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="w", width=180 if c=='Name' else 80)
        self.tree.pack(fill="both", expand=True, padx=4, pady=4)

        ctrl_frame = ttk.Frame(self, width=320)
        ctrl_frame.pack(side="right", fill="y", padx=8, pady=8)

        ttk.Label(ctrl_frame, text="Product ID:").pack(anchor="w")
        self.product_id_entry = ttk.Entry(ctrl_frame)
        self.product_id_entry.pack(fill="x", pady=2)

        ttk.Label(ctrl_frame, text="Quantity:").pack(anchor="w")
        self.qty_entry = ttk.Entry(ctrl_frame)
        self.qty_entry.pack(fill="x", pady=2)

        self.add_btn = ttk.Button(ctrl_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_btn.pack(fill="x", pady=6)

        ttk.Label(ctrl_frame, text="Cart:").pack(anchor="w", pady=(10,0))
        self.cart_box = tk.Listbox(ctrl_frame, height=10)
        self.cart_box.pack(fill="both", pady=4)

        self.total_var = tk.StringVar(value="Total: $0.00")
        ttk.Label(ctrl_frame, textvariable=self.total_var).pack(pady=4)

        self.confirm_btn = ttk.Button(ctrl_frame, text="Confirm Order", command=self.confirm_order)
        self.confirm_btn.pack(fill="x", pady=6)

        self.restock_btn = ttk.Button(ctrl_frame, text="Restock from restock.csv", command=self.restock)
        self.restock_btn.pack(fill="x", pady=6)

        self.search_var = tk.StringVar()
        ttk.Label(ctrl_frame, text="Search product name:").pack(anchor="w", pady=(10,0))
        self.search_entry = ttk.Entry(ctrl_frame, textvariable=self.search_var)
        self.search_entry.pack(fill="x", pady=2)
        self.search_entry.bind("<KeyRelease>", lambda e: self.refresh_products())

        self.refresh_btn = ttk.Button(ctrl_frame, text="Refresh Products", command=self.refresh_products)
        self.refresh_btn.pack(fill="x", pady=6)

    def refresh_products(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        q = self.search_var.get().lower().strip()
        for p in self.inventory.products:
            if q and q not in p['name'].lower():
                continue
            self.tree.insert("", "end", values=(p['id'], p['name'], f"${float(p['price']):.2f}", p['stock']))

    def add_to_cart(self):
        try:
            pid = int(self.product_id_entry.get().strip())
            qty = int(self.qty_entry.get().strip())
        except ValueError:
            messagebox.showerror("Input error", "Please enter numeric Product ID and Quantity.")
            return
        success, msg = self.order.add_to_cart(pid, qty)
        if not success:
            messagebox.showerror("Error", msg)
            return
        self.update_cart_display()
        self.refresh_products()

    def update_cart_display(self):
        self.cart_box.delete(0, "end")
        for item in self.order.cart:
            self.cart_box.insert("end", f"{item['qty']} x {item['name']} @ ${item['price']:.2f} = ${item['price']*item['qty']:.2f}")
        total = self.order.calculate_subtotal()
        self.total_var.set(f"Total: ${total:.2f}")

    def confirm_order(self):
        if not self.order.cart:
            messagebox.showinfo("Cart empty", "No items in cart.")
            return
        customer = simpledialog.askstring("Customer", "Enter customer name (optional):")
        self.order.checkout(customer_name=customer)
        self.report.save_order(self.order.last_order_record)
        messagebox.showinfo("Order confirmed", "Order processed and saved.")
        self.order.clear_cart()
        self.update_cart_display()
        self.refresh_products()

    def restock(self):
        added = self.inventory.restock_from_csv("restock.csv")
        messagebox.showinfo("Restock", f"Restocked {added} product lines from restock.csv")
        self.refresh_products()

if __name__ == "__main__":
    app = App()
    app.mainloop()
