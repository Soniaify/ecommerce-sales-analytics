
import pandas as pd

# Load dataset
df = pd.read_excel("data/Online Retail.xlsx")

# 1. Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# 2. Check negative quantities
print("\nNEGATIVE QUANTITIES")
print(df[df["Quantity"] < 0].head(10))

print("\nTOTAL NEGATIVE QUANTITIES")
print((df["Quantity"] < 0).sum())

# 3. Check negative prices
print("\nNEGATIVE UNIT PRICES")
print(df[df["UnitPrice"] < 0].head(10))

print("\nTOTAL NEGATIVE PRICES")
print((df["UnitPrice"] < 0).sum())

# 4. Check cancelled invoices
print("\nCANCELLED INVOICES")
cancelled = df[df["InvoiceNo"].astype(str).str.startswith("C")]
print(cancelled.head(10))

print("\nTOTAL CANCELLED INVOICES")
print(cancelled.shape[0])

# 5. Check missing customer IDs
print("\nMISSING CUSTOMER IDs")
print(df[df["CustomerID"].isnull()].head(10))
