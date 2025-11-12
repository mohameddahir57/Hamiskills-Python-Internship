
import pandas as pd
from pathlib import Path

def load_sales_from_folder(folder_path):
    folder = Path(folder_path)
    files = list(folder.glob('sales_*.csv'))
    if not files:
        raise FileNotFoundError(f'No sales files found in {folder_path}')
    dfs = [pd.read_csv(f) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
    df['line_total'] = pd.to_numeric(df['line_total'], errors='coerce').fillna(df['quantity'] * df['unit_price'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
