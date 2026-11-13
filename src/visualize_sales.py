
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

os.makedirs("reports", exist_ok=True)

# Load reports
monthly = pd.read_csv("reports/monthly_sales.csv")
products = pd.read_csv("reports/top_products.csv")
countries = pd.read_csv("reports/country_sales.csv")


# Format revenue labels
def format_currency(value):
    if value >= 1_000_000:
        return f"£{value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"£{value / 1_000:.1f}K"
    return f"£{value:.0f}"


# 1. MONTHLY SALES REVENUE
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    monthly["Month"],
    monthly["Total_Revenue"],
    marker="o",
    linewidth=2
)

ax.set_title("Monthly Sales Revenue", fontsize=16)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (£)")
ax.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: format_currency(x))
)

ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.3)

ax.annotate(
    "December is incomplete",
    xy=(12, monthly.iloc[-1]["Total_Revenue"]),
    xytext=(-110, 25),
    textcoords="offset points",
    arrowprops={"arrowstyle": "->"}
)

plt.tight_layout()
plt.savefig("reports/monthly_sales.png", dpi=300)
plt.close()


# 2. TOP 10 COUNTRIES
def create_country_chart(data, filename, title):
    data = data.sort_values("Total_Revenue")

    fig, ax = plt.subplots(figsize=(12, 7))

    bars = ax.barh(
        data["Country"],
        data["Total_Revenue"]
    )

    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Revenue (£)")
    ax.set_ylabel("Country")

    ax.xaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, _: format_currency(x))
    )

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f"  {format_currency(width)}",
            va="center"
        )

    plt.tight_layout()
    plt.savefig(f"reports/{filename}", dpi=300)
    plt.close()


create_country_chart(
    countries,
    "country_sales.png",
    "Top 10 Countries by Revenue"
)

# Compare other countries without the UK
other_countries = countries[
    countries["Country"] != "United Kingdom"
]

create_country_chart(
    other_countries,
    "country_sales_excluding_uk.png",
    "Top 9 Countries by Revenue (Excluding UK)"
)


# 3. TOP 10 PHYSICAL PRODUCTS
merchandise = products[
    ~products["Description"].str.contains(
        r"POSTAGE|^MANUAL$",
        case=False,
        na=False
    )
].copy()

merchandise = merchandise.sort_values(
    "Total_Revenue",
    ascending=True
)

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(
    merchandise["Description"],
    merchandise["Total_Revenue"]
)

ax.set_title("Top Physical Products by Revenue", fontsize=16)
ax.set_xlabel("Revenue (£)")
ax.set_ylabel("Product")

ax.xaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: format_currency(x))
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f"  {format_currency(width)}",
        va="center"
    )

plt.tight_layout()
plt.savefig("reports/top_products.png", dpi=300)
plt.close()

print("UPDATED CHARTS CREATED SUCCESSFULLY")
print("Check your reports folder.")
