
import pandas as pd

# Load the retail dataset
file_path = "data/Online Retail.xlsx"

df = pd.read_excel(file_path)

# Display the first five records
print("\nFIRST FIVE RECORDS")
print(df.head())

# Display dataset dimensions
print("\nDATASET SHAPE")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Display data types and missing values
print("\nDATASET INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

# Display basic statistics
print("\nSUMMARY STATISTICS")
print(df.describe())
