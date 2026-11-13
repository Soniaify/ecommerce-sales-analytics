
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)

# Load segmented customer data
rfm = pd.read_csv("reports/customer_segments.csv")

# 1. CUSTOMER DISTRIBUTION
segment_counts = rfm["Segment"].value_counts()

fig, ax = plt.subplots(figsize=(11, 6))

bars = ax.bar(
    segment_counts.index,
    segment_counts.values
)

ax.set_title("Customer Distribution by Segment", fontsize=16)
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.tick_params(axis="x", rotation=35)

for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height()):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("reports/customer_distribution.png", dpi=300)
plt.close()


# 2. REVENUE BY CUSTOMER SEGMENT
segment_revenue = rfm.groupby("Segment")["Monetary"].sum()
segment_revenue = segment_revenue.sort_values()

fig, ax = plt.subplots(figsize=(11, 6))

bars = ax.barh(
    segment_revenue.index,
    segment_revenue.values
)

ax.set_title("Revenue Contribution by Customer Segment", fontsize=16)
ax.set_xlabel("Revenue (£)")
ax.set_ylabel("Customer Segment")

for bar in bars:
    value = bar.get_width()

    ax.text(
        value,
        bar.get_y() + bar.get_height() / 2,
        f" £{value:,.0f}",
        va="center"
    )

plt.tight_layout()
plt.savefig("reports/customer_segment_revenue.png", dpi=300)
plt.close()

print("CUSTOMER VISUALISATIONS CREATED SUCCESSFULLY")
print("1. customer_distribution.png")
print("2. customer_segment_revenue.png")
