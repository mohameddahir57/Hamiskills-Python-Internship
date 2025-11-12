
Hami MiniMarket Sales Dashboard & Analytics (Capstone)
-----------------------------------------------------
Structure:
- data/                sample sales_YYYY-MM-DD.csv files
- src/                 Python modules (data_loader, analytics, visuals, main)
- charts/              generated PNG charts


How to run:
1. Create a virtual environment and install requirements:
   pip install pandas matplotlib
2. From the project root, run:
   python -m src.main

Notes:
- This project reads all files matching data/sales_*.csv and combines them.
- The visuals are saved into charts/ and summary CSVs into output/.
