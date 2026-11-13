
import pandas as pd
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_online_retail.csv",
    dtype={"InvoiceNo": str, "StockCode": str},
    parse_dates=["InvoiceDate"]
)

# 1. MONTHLY SALES ANALYSIS
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("InvoiceNo", "nunique")
).reset_index()

monthly_sales["Total_Revenue"] = monthly_sales["Total_Revenue"].round(2)

print("\nMONTHLY SALES PERFORMANCE")
print(monthly_sales.to_string(index=False))

monthly_sales.to_csv("reports/monthly_sales.csv", index=False)


# 2. TOP 10 PRODUCTS BY REVENUE
top_products = df.groupby("Description").agg(
    Total_Revenue=("Revenue", "sum"),
    Units_Sold=("Quantity", "sum")
).sort_values(
    "Total_Revenue", ascending=False
).head(10).reset_index()

top_products["Total_Revenue"] = top_products["Total_Revenue"].round(2)

print("\nTOP 10 PRODUCTS")
print(top_products.to_string(index=False))

top_products.to_csv("reports/top_products.csv", index=False)


# 3. TOP 10 COUNTRIES BY REVENUE
country_sales = df.groupby("Country").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Orders=("InvoiceNo", "nunique")
).sort_values(
    "Total_Revenue", ascending=False
).head(10).reset_index()

country_sales["Total_Revenue"] = country_sales["Total_Revenue"].round(2)

print("\nTOP 10 COUNTRIES")
print(country_sales.to_string(index=False))

country_sales.to_csv("reports/country_sales.csv", index=False)


# 4. GENERAL BUSINESS SUMMARY
print("\nBUSINESS SUMMARY")
print("Total Revenue:", round(df["Revenue"].sum(), 2))
print("Total Orders:", df["InvoiceNo"].nunique())
print("Total Products:", df["StockCode"].nunique())
print("Total Countries:", df["Country"].nunique())
print("Total Units Sold:", df["Quantity"].sum())

print("\nSALES ANALYSIS COMPLETED")
print("Reports saved inside the reports folder.")
