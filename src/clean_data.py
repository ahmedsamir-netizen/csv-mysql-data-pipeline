import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

file_path = DATA_DIR / "sales_data.csv"
clean_file_path = DATA_DIR / "clean_sales_data.csv"

df = pd.read_csv(file_path)


#clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#clean dates 
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

#cahnge data types for numeric columns, coercing errors to NaN
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce', downcast='integer')
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')
df['profit'] = pd.to_numeric(df['profit'], errors='coerce')


#drop null values
df = df.dropna()

#save cleaned data to new CSV
df.to_csv(clean_file_path, index=False)
print(f"Clean data saved successfully: {clean_file_path}")