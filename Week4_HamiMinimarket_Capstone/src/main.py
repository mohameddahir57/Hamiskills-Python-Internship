
from pathlib import Path
from src.data_loader import load_sales_from_folder
from src.analytics import calculate_key_metrics, export_summary_csv
from src.visuals import plot_daily_trends, plot_product_popularity

def run(data_folder='data', charts_folder='charts', out_folder='output'):
    data_folder = Path(data_folder)
    charts_folder = Path(charts_folder)
    out_folder = Path(out_folder)
    out_folder.mkdir(exist_ok=True)
    df = load_sales_from_folder(data_folder)
    if df.empty:
        print('No data loaded. Exiting.')
        return
    summary = calculate_key_metrics(df)
    # export summary files
    export_summary_csv(summary, out_folder)
    # generate visuals
    daily = summary.get('daily_trends')
    # ensure date column name consistent with visuals (date)
    if 'date' in daily.columns and daily['date'].dtype.name.startswith('datetime'):
        daily['date'] = daily['date'].dt.date
    p1 = plot_daily_trends(daily, charts_folder)
    p2 = plot_product_popularity(summary.get('top_products'), charts_folder)
    print('Generated charts:', p1, p2)
    print('Summary metrics saved to', out_folder / 'summary_metrics.csv')

if __name__ == '__main__':
    run(data_folder='../data', charts_folder='../charts', out_folder='../output')
