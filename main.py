import matplotlib.pyplot as plt
import pandas as pd

# Load the sales dataset
data = pd.read_csv("data/sales.csv")

# Display the dataset
print(data)
# Display the first 5 rows
print("\nFirst 5 rows:")
print(data.head())

# Display the number of rows and columns
print("\nDataset shape:")
print(data.shape)

# Display column names and data types
print("\nDataset information:")
print(data.info())
# Calculate revenue for each order
data["Revenue"] = data["Quantity"] * data["UnitPrice"]

# Display the updated dataset
print("\nSales data with revenue:")
print(data)
# Calculate total revenue
total_revenue = data["Revenue"].sum()

print("\nTotal Revenue:")
print("Rs.", total_revenue)
# Calculate revenue by product
product_revenue = data.groupby("Product")["Revenue"].sum()

print("\nRevenue by Product:")
print(product_revenue)
# Calculate total quantity sold per product
product_quantity = data.groupby("Product")["Quantity"].sum()

# Find the best-selling product
best_selling = product_quantity.idxmax()

print("\nBest-Selling Product:")
print(best_selling)
# Bar chart: Revenue by Product

plt.figure(figsize=(8, 5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")

plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("images/revenue_by_product.png")

# Display the chart
plt.close()
# Calculate revenue by region
region_revenue = data.groupby("Region")["Revenue"].sum()

# Create a pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    region_revenue,
    labels=region_revenue.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Contribution by Region")

plt.tight_layout()

# Save the chart
plt.savefig("images/revenue_by_region.png")

# Display the chart
plt.close()
# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Extract month
data["Month"] = data["Date"].dt.to_period("M")

# Calculate monthly revenue
monthly_sales = data.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Create a line chart
plt.figure(figsize=(8, 5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o",
    linestyle="-"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.grid(True)

plt.tight_layout()

# Save the chart
plt.savefig("images/monthly_sales_trend.png")

# Display the chart
plt.close()
# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())
# Check duplicate records
print("Duplicate rows:")
print(data.duplicated().sum())
# Remove duplicate rows
data = data.drop_duplicates()

print("Duplicates removed successfully!")
# Check invalid quantities
print("Invalid quantities:")
print(data[data["Quantity"] <= 0])

# Check invalid prices
print("Invalid prices:")
print(data[data["UnitPrice"] <= 0])
# Save cleaned dataset
data.to_csv("data/cleaned_sales.csv", index=False)

print("Cleaned data saved successfully!")
# Step 1: Exploratory Data Analysis

# Load the cleaned data
clean_data = pd.read_csv("data/cleaned_sales.csv")

# Display the first five rows
print("\nCleaned Data:")
print(clean_data.head())

# Total revenue
total_revenue = clean_data["Revenue"].sum()
print("\nTotal Revenue: ₹", total_revenue)

# Revenue by product
product_sales = clean_data.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(product_sales)

# Revenue by region
region_sales = clean_data.groupby("Region")["Revenue"].sum()
print("\nRevenue by Region:")
print(region_sales)

# Best-selling product by quantity
best_product = clean_data.groupby("Product")["Quantity"].sum().idxmax()
print("\nBest-Selling Product:", best_product)

# Monthly revenue
clean_data["Date"] = pd.to_datetime(clean_data["Date"])
clean_data["Month"] = clean_data["Date"].dt.to_period("M")
monthly_sales = clean_data.groupby("Month")["Revenue"].sum()
print("\nMonthly Revenue:")
print(monthly_sales)
# Step 2: Data Visualization

import matplotlib.pyplot as plt

# 1. Revenue by Product
product_sales = clean_data.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar", color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_product.png")
plt.close()


# 2. Revenue by Region
region_sales = clean_data.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Share by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/revenue_by_region.png")
plt.close()


# 3. Monthly Revenue Trend
monthly_sales = clean_data.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/monthly_revenue.png")
plt.close()

print("\nCharts saved successfully in the images folder!")
# Step 3: Generate Sales Report

# Calculate key business insights
total_revenue = clean_data["Revenue"].sum()
total_orders = clean_data["OrderID"].nunique()
average_order_value = total_revenue / total_orders

product_sales = clean_data.groupby("Product")["Revenue"].sum()
region_sales = clean_data.groupby("Region")["Revenue"].sum()

best_product = product_sales.idxmax()
best_region = region_sales.idxmax()

best_selling_product = (
    clean_data.groupby("Product")["Quantity"].sum().idxmax()
)

# Create report
report = f"""
====================================
       SALES ANALYSIS REPORT
====================================

Total Revenue: ₹{total_revenue:,.2f}
Total Orders: {total_orders}
Average Order Value: ₹{average_order_value:,.2f}

------------------------------------
PRODUCT INSIGHTS
------------------------------------

Highest Revenue Product: {best_product}
Best-Selling Product by Quantity: {best_selling_product}

Revenue by Product:
{product_sales.to_string()}

------------------------------------
REGIONAL INSIGHTS
------------------------------------

Highest Revenue Region: {best_region}

Revenue by Region:
{region_sales.to_string()}

------------------------------------
BUSINESS CONCLUSION
------------------------------------

The {best_product} generated the highest revenue.
The {best_selling_product} had the highest sales quantity.
The {best_region} region contributed the most revenue.

====================================
"""

# Save the report
with open("sales_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nSales report generated successfully!")

# Step 4: Advanced Sales Insights

# Average order value
total_revenue = clean_data["Revenue"].sum()
total_orders = clean_data["OrderID"].nunique()

average_order_value = total_revenue / total_orders

print("\n--- ADVANCED SALES INSIGHTS ---")
print(f"Average Order Value: ₹{average_order_value:,.2f}")

# Revenue contribution by product
product_revenue = clean_data.groupby("Product")["Revenue"].sum()

product_contribution = (
    product_revenue / total_revenue * 100
)

print("\nProduct Revenue Contribution (%):")
print(product_contribution.round(2))

# Revenue contribution by region
region_revenue = clean_data.groupby("Region")["Revenue"].sum()

top_region = region_revenue.idxmax()

print("\nTop Performing Region:", top_region)
print("Revenue:", f"₹{region_revenue.max():,.2f}")

# Save insights
insights = pd.DataFrame({
    "Product": product_revenue.index,
    "Revenue": product_revenue.values,
    "Contribution_Percentage": product_contribution.values
})

insights.to_csv("data/product_insights.csv", index=False)

print("\nProduct insights saved successfully!")
