# Create a Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define product categories and regions
categories = ['Makeup', 'School Supplies', 'Electronics']
regions = ['NCR', 'CALABARZON', 'CAR']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Create an empty list to store data
data = []

# Generate sales data for 6 months
for month in months:
    for category in categories:
        for region in regions:
            sales = np.random.randint(1000, 5000)  # Random sales value
            data.append({'Month': month, 'Category': category, 'Region': region, 'Sales': sales})

# Create DataFrame
df = pd.DataFrame(data)

# Introduce missing and inconsistent values
# Missing sales value
df.loc[2, 'Sales'] = np.nan
# Typo in category name
df.loc[7, 'Category'] = 'School Supples'
# Another typo
df.loc[15, 'Category'] = 'Electrnics'
# Make a sales value non-numeric for demonstration
df.loc[20, 'Sales'] = '2500a'

print("Original DataFrame:")
print(df.head(10))
print("\nDataFrame Info (Before Cleaning):")
df.info()

# Clean the data
# Fix category name typos
df['Category'] = df['Category'].replace({'School Supples': 'School Supplies', 'Electrnics': 'Electronics'})

# Convert 'Sales' to numeric, coercing errors to NaN
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# Fill missing sales values with the mean of sales (can also use median or drop)
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

print("\nCleaned DataFrame:")
print(df.head(10))
print("\nDataFrame Info (After Cleaning):")
df.info()

# Ensure 'Month' is ordered for line chart
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Creation & Customization of Charts
# Set a consistent style for all plots
sns.set_style("whitegrid")

# Bar Chart: Total sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum, palette='viridis')
plt.title('Total Sales by Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Line Chart: Sales over months for each region
plt.figure(figsize=(12, 7))
# Aggregate sales by month and region
df_monthly_region = df.groupby(['Month', 'Region'])['Sales'].sum().reset_index()
sns.lineplot(x='Month', y='Sales', hue='Region', data=df_monthly_region, marker='o', palette='plasma')
plt.title('Monthly Sales Trend by Region', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True)
plt.legend(title='Region')
plt.tight_layout()
plt.show()


# Box Plot: Sales distribution by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Sales', data=df, palette='cividis')
plt.title('Sales Distribution by Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Heatmap: Average sales per region per month
plt.figure(figsize=(10, 7))
# Pivot table for heatmap data
df_heatmap = df.pivot_table(index='Region', columns='Month', values='Sales', aggfunc='mean')
sns.heatmap(df_heatmap, annot=True, fmt=".0f", cmap='YlGnBu', linewidths=.5)
plt.title('Average Sales per Region per Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Region', fontsize=12)
plt.tight_layout()
plt.show()

# Bonus
# Calculate total sales per month
total_sales_per_month = df.groupby('Month')['Sales'].sum().reset_index()
highest_sales_month = total_sales_per_month.loc[total_sales_per_month['Sales'].idxmax()]

plt.figure(figsize=(12, 7))
sns.lineplot(x='Month', y='Sales', hue='Region', data=df_monthly_region, marker='o', palette='plasma')
plt.title('Monthly Sales Trend by Region (with Highest Sales Highlight)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True)
plt.legend(title='Region')

# Highlight the month with the highest total sales
plt.annotate(f'Highest Sales: {highest_sales_month["Month"]} ({highest_sales_month["Sales"]:.0f})',
             xy=(highest_sales_month['Month'], highest_sales_month['Sales']),
             xytext=(highest_sales_month['Month'], highest_sales_month['Sales'] + 5000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             ha='center', va='bottom', fontsize=10, color='red')

plt.tight_layout()
# Save the chart as an image
plt.savefig("monthly_sales_trend_highlighted.png")
plt.show()

print("\nChart 'monthly_sales_trend_highlighted.png' saved successfully.")
