
import matplotlib.pyplot as plt
from pathlib import Path

def plot_daily_trends(daily_trends_df, out_folder):
    out_folder = Path(out_folder)
    out_folder.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8,4))
    plt.plot(daily_trends_df['date'], daily_trends_df['daily_total'], marker='o')
    plt.title('Daily Sales Trends')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.tight_layout()
    p = out_folder / 'daily_trends.png'
    plt.savefig(p)
    plt.close()
    return p

def plot_product_popularity(top_products_df, out_folder, top_n=8):
    out_folder = Path(out_folder)
    out_folder.mkdir(parents=True, exist_ok=True)
    df = top_products_df.copy().head(top_n)
    plt.figure(figsize=(8,5))
    plt.bar(df['product_name'] + ' (' + df['product_id'] + ')', df['quantity'])
    plt.title('Top Selling Products')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Quantity Sold')
    plt.tight_layout()
    p = out_folder / 'product_popularity.png'
    plt.savefig(p)
    plt.close()
    return p
