import pandas as pd
from pathlib import Path
from db_connection import get_connection

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
file_path = DATA_DIR / "clean_sales_data.csv"

df = pd.read_csv(file_path)
total_rows = len(df)

conn = get_connection()
cursor = conn.cursor()

success_count = 0
fail_count = 0
failed_rows = []

for _, row in df.iterrows():
    try:
        query = """
        INSERT INTO sales_data (
            row_id, order_id, order_date, ship_date, ship_mode,
            customer_id, customer_name, segment, country_region, city,
            state, postal_code, region, product_id, category, sub_category,
            product_name, sales, quantity, discount, profit
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = tuple(row)
        cursor.execute(query, values)
        success_count += 1
    except Exception as e:
        fail_count += 1
        failed_rows.append((row['order_id'], str(e)))

conn.commit()
cursor.close()
conn.close()

print("=== Data Load Summary ===")
print(f"Total rows processed: {total_rows}")
print(f"Successfully loaded: {success_count}")
print(f"Failed to load: {fail_count}")

if fail_count > 0:
    print("\nFailed rows details:")
    for row_id, error in failed_rows:
        print(f"Order ID {row_id}: {error}")

print("\nData loaded successfully")