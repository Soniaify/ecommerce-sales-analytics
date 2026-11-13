
import pandas as pd
import numpy as np
import os

os.makedirs("reports", exist_ok=True)

# Load RFM data
rfm = pd.read_csv("reports/rfm_customer_metrics.csv")

# Calculate RFM scores
# Recency: lower days = better score
# Frequency and Monetary: higher values = better score

rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)


# Assign customer segments
def segment_customer(row):

    r = row["R_Score"]
    f = row["F_Score"]
    m = row["M_Score"]

    if r >= 3 and f >= 3 and m >= 3:
        return "Champions"

    elif f >= 3 and m >= 3:
        return "Loyal Customers"

    elif r >= 3 and f >= 2:
        return "Potential Loyalists"

    elif r == 4 and f == 1:
        return "New Customers"

    elif r <= 2 and f >= 3:
        return "At Risk"

    elif r <= 2 and f <= 2:
        return "Hibernating"

    else:
        return "Regular Customers"


rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# Save segmented customers
rfm.to_csv("reports/customer_segments.csv", index=False)


# Display segment counts
segment_counts = rfm["Segment"].value_counts()

print("\nCUSTOMER SEGMENT DISTRIBUTION")
print(segment_counts.to_string())


# Revenue contribution by segment
segment_revenue = rfm.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    Total_Revenue=("Monetary", "sum"),
    Average_Spending=("Monetary", "mean")
).sort_values(
    "Total_Revenue",
    ascending=False
)

print("\nREVENUE CONTRIBUTION BY SEGMENT")
print(segment_revenue.round(2).to_string())


print("\nCUSTOMER SEGMENTATION COMPLETED")
print("Report saved to reports/customer_segments.csv")
