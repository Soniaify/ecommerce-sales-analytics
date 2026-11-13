
import pandas as pd

# Load the original dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("ORIGINAL DATASET")
print("Rows:", len(df))

# 1. Remove exact duplicate records
df = df.drop_duplicates()

# 2. Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# 3. Remove records with negative unit prices
df = df[df["UnitPrice"] >= 0]

# 4. Remove records with zero or negative quantities
# We will analyse returns separately later
df = df[df["Quantity"] > 0]

# 5. Remove records with zero unit prices
df = df[df["UnitPrice"] > 0]

# 6. Remove records with missing product descriptions
df = df.dropna(subset=["Description"])

# 7. Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Save cleaned dataset
df.to_csv("data/cleaned_online_retail.csv", index=False)

print("\nCLEANING COMPLETED")
print("Cleaned rows:", len(df))
print("Remaining missing values:")
print(df.isnull().sum())

print("\nTOTAL SALES REVENUE")
print(round(df["Revenue"].sum(), 2))

print("\nCLEANED DATASET SAVED SUCCESSFULLY")
