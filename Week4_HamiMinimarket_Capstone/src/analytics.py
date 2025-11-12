
import pandas as pd
from pathlib import Path

def calculate_key_metrics(df):
    total_revenue = df['line_total'].sum()
    num_orders = df['order_id'].nunique()
    avg_order_value = total_revenue / num_orders if num_orders else 0
    top_products = df.groupby(['product_id','product_name'])['quantity'].sum().reset_index().sort_values('quantity', ascending=False)
    low_stock = top_products.tail(3)
    daily_trends = df.groupby(df['date'].dt.date)['line_total'].sum().reset_index(name='daily_total')
    return {
        'total_revenue': round(total_revenue,2),
        'num_orders': int(num_orders),
        'avg_order_value': round(avg_order_value,2),
        'top_products': top_products,
        'low_stock': low_stock,
        'daily_trends': daily_trends
    }

def export_summary(summary, out_path):
    out = Path(out_path)
    out.mkdir(exist_ok=True)
    pd.DataFrame([
        {'metric':'total_revenue','value':summary['total_revenue']},
        {'metric':'num_orders','value':summary['num_orders']},
        {'metric':'avg_order_value','value':summary['avg_order_value']}
    ]).to_csv(out / 'summary_metrics.csv', index=False)
    summary['top_products'].to_csv(out / 'top_products.csv', index=False)
    summary['low_stock'].to_csv(out / 'low_stock.csv', index=False)
