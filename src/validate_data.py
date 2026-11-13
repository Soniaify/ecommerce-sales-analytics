
import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_online_retail.csv",
    dtype={"InvoiceNo": str, "StockCode": str}
)

print("CLEANED DATA VALIDATION")

print("\n1. DATASET SIZE")
print(df.shape)

print("\n2. DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n3. NEGATIVE OR ZERO QUANTITIES")
print((df["Quantity"] <= 0).sum())

print("\n4. NEGATIVE OR ZERO UNIT PRICES")
print((df["UnitPrice"] <= 0).sum())

print("\n5. MISSING PRODUCT DESCRIPTIONS")
print(df["Description"].isnull().sum())

print("\n6. MISSING CUSTOMER IDs")
print(df["CustomerID"].isnull().sum())

print("\n7. CANCELLED INVOICES")
print(
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .sum()
)

print("\nVALIDATION COMPLETED")
