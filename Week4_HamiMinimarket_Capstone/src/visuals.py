
import matplotlib.pyplot as plt
from pathlib import Path

def plot_daily_trends(daily_df, out_folder):
    out = Path(out_folder); out.mkdir(exist_ok=True)
    plt.figure(figsize=(8,4))
    plt.plot(daily_df['date'], daily_df['daily_total'], marker='o')
    plt.title('Daily Sales Trends')
    plt.xlabel('Date'); plt.ylabel('Revenue')
    plt.tight_layout()
    plt.savefig(out / 'daily_trends.png'); plt.close()

def plot_product_popularity(top_df, out_folder):
    out = Path(out_folder); out.mkdir(exist_ok=True)
    plt.figure(figsize=(8,4))
    plt.bar(top_df['product_name'], top_df['quantity'])
    plt.title('Top Selling Products')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out / 'product_popularity.png'); plt.close()
