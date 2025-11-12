
from src.data_loader import load_sales_from_folder
from src.analytics import calculate_key_metrics, export_summary
from src.visuals import plot_daily_trends, plot_product_popularity

def run(data_folder='data', charts_folder='charts', out_folder='output'):
    df = load_sales_from_folder(data_folder)
    summary = calculate_key_metrics(df)
    export_summary(summary, out_folder)
    plot_daily_trends(summary['daily_trends'], charts_folder)
    plot_product_popularity(summary['top_products'], charts_folder)
    print('✅ Charts and summary generated successfully!')

if __name__ == '__main__':
    run()
