# Generating and Reading the Datasets
import pandas as pd
import numpy as np
import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

# Customer Data (CSV)
customer_data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Name': ['Alice Smith ', 'Bob Johnson', '  Charlie Brown', 'Diana Prince', 'Eve Davis', 'Frank White', 'Grace Taylor', 'Henry Wilson', 'Ivy Moore', 'Jack Green', 'Alice Smith', 'Bob Johnson'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'diana@example.com', 'eve@example.com', 'frank@example.com', 'grace@example.com', 'henry@example.com', 'ivy@example.com', 'jack@example.com', 'alice@example.com', 'bob@example.com'],
    'Phone': ['111-222-3333', '222-333-4444', '333-444-5555', '444-555-6666', '555-666-7777', '666-777-8888', '777-888-9999', '888-999-0000', '999-000-1111', '000-111-2222', '111-222-3333', '222-333-4444'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm St', '202 Maple Dr', '303 Birch Rd', '404 Cedar Blvd', '505 Willow Way', '606 Spruce Ct', '707 Poplar Pl', '123 Main St', '456 Oak Ave'],
    'JoinDate': ['2022-01-15', '2021-11-20', '2023-03-10', '2022-07-01', '2021-09-05', '2023-01-25', '2022-04-12', '2021-10-30', '2023-02-18', '2022-06-01', '2022-01-15', '2021-11-20'],
    'Age': [25, 30, np.nan, 40, 35, 28, 45, 50, 22, 33, 25, 30]
}
customer_df = pd.DataFrame(customer_data)
customer_df.to_csv('customers.csv', index=False)

# Sales Data (Excel)
sales_data = {
    'SaleID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headphones', 'Speaker', 'Microphone', 'Printer', 'Router', 'Laptop', 'Mouse'],
    'Quantity': [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2],
    'Price': [1200.00, 25.00, 75.00, 300.00, 50.00, 80.00, 150.00, 60.00, 200.00, 90.00, 1200.00, 25.00],
    'SaleDate': ['2023-01-20', '2023-01-22', '2023-02-01', '2023-02-05', '2023-03-10', '2023-03-12', '2023-04-01', '2023-04-03', '2023-05-01', '2023-05-05', '2023-01-20', '2023-01-22'],
    'Discount': [0.1, 0.05, 0.0, 0.15, 0.0, 0.1, 0.0, 0.05, 0.0, 0.1, 0.1, 0.05]
}
sales_df = pd.DataFrame(sales_data)
sales_df.to_excel('sales.xlsx', index=False)

# Reviews Data (JSON)
reviews_data = [
    {"review_id": 1001, "customer_id": 1, "product": "Laptop", "rating": 5, "comment": "Excellent product!"},
    {"review_id": 1002, "customer_id": 2, "product": "Mouse", "rating": 4, "comment": "Good value for money."},
    {"review_id": 1003, "customer_id": 3, "product": "Keyboard", "rating": 5, "comment": "Very comfortable to type."},
    {"review_id": 1004, "customer_id": 4, "product": "Monitor", "rating": 3, "comment": "Screen could be brighter. "},
    {"review_id": 1005, "customer_id": 5, "product": "Webcam", "rating": 4, "comment": "Clear video quality."},
    {"review_id": 1006, "customer_id": 6, "product": "Headphones", "rating": 5, "comment": "Great sound!"},
    {"review_id": 1007, "customer_id": 7, "product": "Speaker", "rating": 4, "comment": "Decent bass."},
    {"review_id": 1008, "customer_id": 8, "product": "Microphone", "rating": 2, "comment": "Static noise present."},
    {"review_id": 1009, "customer_id": 9, "product": "Printer", "rating": 5, "comment": "Fast and efficient."},
    {"review_id": 1010, "customer_id": 10, "product": "Router", "rating": 4, "comment": "Easy to set up. "},
    {"review_id": 1001, "customer_id": 1, "product": "Laptop", "rating": 5, "comment": "Excellent product!"} # Duplicate
]
with open('reviews.json', 'w') as f:
    json.dump(reviews_data, f, indent=4)

# Read and Display Data
df_customers = pd.read_csv('customers.csv')
df_sales = pd.read_excel('sales.xlsx')
df_reviews = pd.read_json('reviews.json')

print("--- Customers Data (First 5 rows) ---")
print(df_customers.head())
print("\n--- Sales Data (First 5 rows) ---")
print(df_sales.head())
print("\n--- Reviews Data (First 5 rows) ---")
print(df_reviews.head())

# Optional Web Scraping
# Dummy HTML file for web scraping
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Retail Company Promotions</title>
</head>
<body>
    <h1>Welcome to Our Store!</h1>
    <p>Check out our latest promotions:</p>
    <ul>
        <li><strong>Summer Sale:</strong> Up to 30% off on selected electronics!</li>
        <li><strong>New Customer Offer:</strong> 10% off your first purchase.</li>
        <li>Free shipping on all orders over $100.</li>
    </ul>
    <div class="contact-info">
        <p>Contact us at: info@retailco.com</p>
        <p>Phone: 1-800-RET-AIL</p>
    </div>
</body>
</html>
"""
with open("promotions.html", "w") as file:
    file.write(html_content)

# Performing Web Scraping
try:
    with open("promotions.html", "r") as file:
        html_doc = file.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    print("\n--- Web Scraping Output ---")
    print("Page Title:", soup.title.string)

    promotions = soup.find_all('li')
    print("\nPromotions:")
    for promo in promotions:
        print("-", promo.get_text())

    contact_info = soup.find('div', class_='contact-info')
    if contact_info:
        print("\nContact Information:")
        print(contact_info.get_text(separator='\n'))
except Exception as e:
    print(f"Error during web scraping: {e}")

# Data Cleaning
print("\nBefore Data Cleaning")
print("\nCustomers Info:")
print(df_customers.info())
print("\nMissing values in Customers:\n", df_customers.isnull().sum())
print("\nDuplicate rows in Customers:\n", df_customers.duplicated().sum())

print("\nReviews Info:")
print(df_reviews.info())
print("\nMissing values in Reviews:\n", df_reviews.isnull().sum())
print("\nDuplicate rows in Reviews:\n", df_reviews.duplicated().sum())

# Fix missing values (Customers)
# Fill in missing values with the median age.
df_customers['Age'].fillna(df_customers['Age'].median(), inplace=True)
print("\nCustomers: Missing 'Age' values after filling with median:")
print(df_customers.isnull().sum())

# Fix extra spaces
for col in ['Name', 'Email', 'Address']:
    if df_customers[col].dtype == 'object':
        df_customers[col] = df_customers[col].str.strip()

for col in ['product', 'comment']:
    if df_reviews[col].dtype == 'object':
        df_reviews.loc[:, col] = df_reviews[col].str.strip()

# Remove duplicates
df_customers.drop_duplicates(inplace=True)
df_reviews.drop_duplicates(inplace=True)
df_sales.drop_duplicates(inplace=True)


print("\nAfter Data Cleaning")
print("\nCustomers Info (after cleaning):")
print(df_customers.info())
print("\nMissing values in Customers (after cleaning):\n", df_customers.isnull().sum())
print("\nDuplicate rows in Customers (after cleaning):\n", df_customers.duplicated().sum())

print("\nReviews Info (after cleaning):")
print(df_reviews.info())
print("\nMissing values in Reviews (after cleaning):\n", df_reviews.isnull().sum())
print("\nDuplicate rows in Reviews (after cleaning):\n", df_reviews.duplicated().sum())

print("\nSales Info (after cleaning):")
print(df_sales.info())
print("\nDuplicate rows in Sales (after cleaning):\n", df_sales.duplicated().sum())

print("\nCustomers Data (first 5 rows after cleaning):")
print(df_customers.head())
print("\nReviews Data (first 5 rows after cleaning):")
print(df_reviews.head())

# Data Transformation
print("\nBefore Data Transformation (Data Types)")
print("\nCustomers Dtypes:\n", df_customers.dtypes)
print("\nSales Dtypes:\n", df_sales.dtypes)
print("\nReviews Dtypes:\n", df_reviews.dtypes)

# Convert Data Types
# Convert 'JoinDate' to datetime in df_customers
df_customers['JoinDate'] = pd.to_datetime(df_customers['JoinDate'])

# Convert 'SaleDate' to datetime in df_sales
df_sales['SaleDate'] = pd.to_datetime(df_sales['SaleDate'])

# Convert 'rating' to int in df_reviews
df_reviews['rating'] = df_reviews['rating'].astype(int)

print("\n--- After Data Transformation (Data Types) ---")
print("\nCustomers Dtypes:\n", df_customers.dtypes)
print("\nSales Dtypes:\n", df_sales.dtypes)
print("\nReviews Dtypes:\n", df_reviews.dtypes)

# Rename columns
df_customers.rename(columns={'Name': 'CustomerName', 'Email': 'CustomerEmail'}, inplace=True)
df_sales.rename(columns={'Price': 'UnitPrice'}, inplace=True)
df_reviews.rename(columns={'comment': 'ReviewComment'}, inplace=True)

print("\nAfter Column Renaming")
print("\nCustomers Columns:", df_customers.columns.tolist())
print("Sales Columns:", df_sales.columns.tolist())
print("Reviews Columns:", df_reviews.columns.tolist())

# Create New Metrics
df_sales['TotalSales'] = df_sales['UnitPrice'] * df_sales['Quantity'] * (1 - df_sales['Discount'])

# Calculate 'YearsAsCustomer' in df_customers
current_date = pd.to_datetime('2024-01-01')
df_customers['YearsAsCustomer'] = (current_date - df_customers['JoinDate']).dt.days / 365.25

# Calculate 'MonthlySales' from 'TotalSales' (Sales per month)
df_sales['SaleMonth'] = df_sales['SaleDate'].dt.to_period('M')
monthly_sales = df_sales.groupby('SaleMonth')['TotalSales'].sum().reset_index()
monthly_sales.rename(columns={'TotalSales': 'MonthlyTotalSales'}, inplace=True)

print("\nAfter Derived Metric Calculations")
print("\nSales Data (with TotalSales - first 5 rows):")
print(df_sales.head())
print("\nCustomers Data (with YearsAsCustomer - first 5 rows):")
print(df_customers.head())
print("\nMonthly Sales (first 5 rows):")
print(monthly_sales.head())

# Merging Datasets
# Rename columns in df_reviews to match other dataframes for merging
df_reviews.rename(columns={'customer_id': 'CustomerID', 'product': 'Product'}, inplace=True)

# Merge customers and sales on 'CustomerID'
df_merged = pd.merge(df_customers, df_sales, on='CustomerID', how='left')

# Merge the result with reviews on 'CustomerID' and 'Product'
df_merged = pd.merge(df_merged, df_reviews, on=['CustomerID', 'Product'], how='left')

print("\n Merged DataFrame (First 5 rows)")
print(df_merged.head())
print("\nMerged DataFrame Info")
print(df_merged.info())

# Analysis via Visualization
# Visualization 1: Distribution of Customer Age (Before vs. After NaN Handling)
plt.figure(figsize=(10, 5))
sns.histplot(df_customers['Age'], bins=5, kde=True)
plt.title('Distribution of Customer Age (After NaN Handling)')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.grid(True)
plt.show()

# Visualization 2: Total Sales Distribution (After 'TotalSales' Calculation)
plt.figure(figsize=(10, 5))
sns.histplot(df_sales['TotalSales'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Total Sales per Transaction')
plt.xlabel('Total Sales ($)')
plt.ylabel('Number of Transactions')
plt.grid(True)
plt.show()

# Visualization 3: Average Rating per Product (After Type Conversion and Cleaning)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
avg_rating_per_product = df_reviews.groupby('Product')['rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_rating_per_product.index, y=avg_rating_per_product.values, palette='viridis')
plt.title('Average Customer Rating per Product')
plt.xlabel('Product')
plt.ylabel('Average Rating')
plt.ylim(0, 5) # Ratings are usually 1-5
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visualization 4: Monthly Total Sales (After Monthly Metric Calculation)
# Convert 'SaleMonth' from Period to Datetime for plotting
monthly_sales['SaleMonth'] = monthly_sales['SaleMonth'].astype('datetime64[ns]')

plt.figure(figsize=(12, 6))
sns.lineplot(x='SaleMonth', y='MonthlyTotalSales', data=monthly_sales, marker='o')
plt.title('Total Sales Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("\n--- Visualizations demonstrate successful data cleaning and transformation. ---")
