
import pandas as pd
import os

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_online_retail.csv",
    dtype={"InvoiceNo": str, "StockCode": str},
    parse_dates=["InvoiceDate"]
)

# Remove records without customer IDs for customer analysis
df = df.dropna(subset=["CustomerID"]).copy()

# Convert customer IDs to integers
df["CustomerID"] = df["CustomerID"].astype(int)

# Set reference date to one day after the last transaction
reference_date = df["InvoiceDate"].max().normalize() + pd.Timedelta(days=1)

# Calculate RFM metrics for each customer
rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (reference_date - x.max().normalize()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

# Round monetary values
rfm["Monetary"] = rfm["Monetary"].round(2)

# Sort customers by highest spending
rfm = rfm.sort_values("Monetary", ascending=False)

# Save results
rfm.to_csv("reports/rfm_customer_metrics.csv", index=False)

# Display results
print("\nRFM ANALYSIS COMPLETED")

print("\nTOTAL CUSTOMERS ANALYSED")
print(len(rfm))

print("\nTOP 10 CUSTOMERS BY SPENDING")
print(rfm.head(10).to_string(index=False))

print("\nRFM SUMMARY")
print(rfm[["Recency", "Frequency", "Monetary"]].describe().round(2))

print("\nRFM REPORT SAVED SUCCESSFULLY")
