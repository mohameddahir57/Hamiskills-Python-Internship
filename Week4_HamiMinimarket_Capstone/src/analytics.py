import pandas as pd
def calculate_key_metrics(df):
    if df.empty:
        return {}
    total_revenue = df['line_total'].sum()
    num_orders = df['order_id'].nunique()
    avg_order_value = total_revenue / num_orders if num_orders else 0.0
    top_products = (df.groupby(['product_id','product_name'])['quantity']
                    .sum().reset_index().sort_values('quantity', ascending=False))
    low_stock = top_products.tail(3)  # placeholder: actual stock not provided - return least sold
    daily_trends = (df.groupby(df['date'].dt.date)['line_total'].sum().reset_index(name='daily_total'))
    summary = {
        'total_revenue': round(float(total_revenue),2),
        'num_orders': int(num_orders),
        'avg_order_value': round(float(avg_order_value),2),
        'top_products': top_products,
        'low_stock_candidates': low_stock,
        'daily_trends': daily_trends
    }
    return summary

def export_summary_csv(summary, out_path):
    parts = []
    parts.append({'metric':'total_revenue','value': summary.get('total_revenue',0)})
    parts.append({'metric':'num_orders','value': summary.get('num_orders',0)})
    parts.append({'metric':'avg_order_value','value': summary.get('avg_order_value',0)})
    df_meta = pd.DataFrame(parts)
    df_meta.to_csv(out_path / 'summary_metrics.csv', index=False)
    # export top products
    summary.get('top_products', pd.DataFrame()).to_csv(out_path / 'top_products.csv', index=False)
    summary.get('low_stock_candidates', pd.DataFrame()).to_csv(out_path / 'low_stock.csv', index=False)
