import pandas as pd
from db_connection import get_connection

conn = get_connection()
df = pd.read_sql("SELECT * FROM sales_data LIMIT 10;", conn)
print(df.head())
conn.close()