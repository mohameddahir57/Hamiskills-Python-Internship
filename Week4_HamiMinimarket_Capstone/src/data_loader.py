
import pandas as pd
import glob
from pathlib import Path

def load_sales_from_folder(folder_path):
    folder = Path(folder_path)
    files = list(folder.glob('sales_*.csv'))
    if not files:
        raise FileNotFoundError(f'No sales files found in {folder_path}')
    dfs = []
    for f in files:
        try:
            df = pd.read_csv(f)
            dfs.append(df)
        except Exception as e:
            print(f'Warning: failed to read {f}: {e}')
    if not dfs:
        return pd.DataFrame()
    combined = pd.concat(dfs, ignore_index=True)
    # handle missing columns gracefully
    expected = ['order_id','date','product_id','product_name','quantity','unit_price','line_total']
    for col in expected:
        if col not in combined.columns:
            combined[col] = pd.NA
    # convert types
    combined['quantity'] = pd.to_numeric(combined['quantity'], errors='coerce').fillna(0).astype(int)
    combined['unit_price'] = pd.to_numeric(combined['unit_price'], errors='coerce').fillna(0.0)
    combined['line_total'] = pd.to_numeric(combined['line_total'], errors='coerce').fillna(combined['quantity'] * combined['unit_price'])
    combined['date'] = pd.to_datetime(combined['date'], errors='coerce')
    combined.sort_values('date', inplace=True)
    return combined
