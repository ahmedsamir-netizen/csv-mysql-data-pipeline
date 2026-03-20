import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
file_path = DATA_DIR / "clean_sales_data.csv"
SAVE_DIR = BASE_DIR / "assets"

#read the cleaned data
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")


# Visualization 1: Total Sales by Category
sales_by_category = df.groupby('category')['sales'].sum()
plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(SAVE_DIR / 'sales_by_category.png')
plt.show()

# Visualization 2: Profit vs Sales
plt.figure(figsize=(8,5))
plt.scatter(df['sales'], df['profit'], alpha=0.6, color='green')
plt.title('Profit vs Sales')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig(SAVE_DIR / 'profit_vs_sales.png')
plt.show()

# Visualization 3: Sales Over Time
df['order_date'] = pd.to_datetime(df['order_date'])
sales_over_time = df.groupby('order_date')['sales'].sum()
plt.figure(figsize=(10,6))
sales_over_time.plot()
plt.title('Sales Over Time')
plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(SAVE_DIR / 'sales_over_time.png')
plt.show()


# Visualization 4: Quantity Sold by Sub-Category
quantity_by_subcategory = df.groupby('sub_category')['quantity'].sum()
plt.figure(figsize=(10,6))
quantity_by_subcategory.plot(kind='bar', color='orange')
plt.title('Quantity Sold by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(SAVE_DIR / 'quantity_by_subcategory.png')
plt.show()

# Visualization 5: Discount vs Profit
plt.figure(figsize=(8,5))
plt.scatter(df['discount'], df['profit'], alpha=0.6, color='red')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig(SAVE_DIR / 'discount_vs_profit.png')
plt.show()

# Visualization 6: Revenue Trend
df['order_date'] = pd.to_datetime(df['order_date'])
revenue_trend = df.groupby('order_date')['sales'].sum()
plt.figure(figsize=(10,6))
revenue_trend.plot()
plt.title('Revenue Trend')
plt.xlabel('Order Date')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig(SAVE_DIR / 'revenue_trend.png')
plt.show()


print("Visualizations saved as PNG in the assets folder.")