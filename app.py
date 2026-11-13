import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="E-commerce Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 E-commerce Sales Analytics Dashboard")

st.markdown("""
Welcome to the E-commerce Sales Analytics Dashboard.

Explore sales performance, customer behaviour,
product performance and revenue forecasts.
""")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Business Overview",
        "Sales Analysis",
        "Customer Segmentation",
        "Sales Forecasting"
    ]
)

# Business Overview
if page == "Business Overview":

    st.header("Business Overview")

    monthly_sales = pd.read_csv(
        "reports/monthly_sales.csv",
        parse_dates=["Month"]
    )

    customer_data = pd.read_csv(
        "reports/rfm_customer_metrics.csv"
    )

    total_revenue = monthly_sales["Total_Revenue"].sum()
    total_orders = monthly_sales["Total_Orders"].sum()
    total_products = 3922
    total_customers = len(customer_data)

    st.subheader("Sales Summary")

    st.write(
        f"Your business generated £{total_revenue:,.2f} "
        f"from {total_orders:,} orders across "
        f"{total_products:,} unique products."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
    col2.metric("Total Orders", f"{total_orders:,}")
    col3.metric("Unique Products", f"{total_products:,}")
    col4.metric("Identifiable Customers", f"{total_customers:,}")

    st.caption(
        "Note: Revenue represents positive sales transactions. "
        "Returns and cancellations were excluded during cleaning."
    )

# Sales Analysis
elif page == "Sales Analysis":

    st.header("Sales Performance Analysis")

    # Load monthly sales report
    monthly_sales = pd.read_csv(
        "reports/monthly_sales.csv",
        parse_dates=["Month"]
    )

    st.subheader("Monthly Revenue Trend")

    st.line_chart(
        monthly_sales,
        x="Month",
        y="Total_Revenue"
    )

    st.subheader("Top 10 Products by Revenue")

    top_products = pd.read_csv("reports/top_products.csv")

    st.bar_chart(
    top_products.head(10),
    x="Description",
    y="Total_Revenue"
)
    st.subheader("Top 10 Countries by Revenue")

    country_sales = pd.read_csv("reports/country_sales.csv")

    st.bar_chart(
        country_sales.head(10),
        x="Country",
        y="Total_Revenue"
    )

    st.dataframe(
        monthly_sales,
        use_container_width=True
    )

# Customer Segmentation
elif page == "Customer Segmentation":

    st.header("Customer Segmentation Analysis")

    segments = pd.read_csv("reports/customer_segments.csv")

    st.subheader("Customer Distribution by Segment")

    segment_counts = (
        segments["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "Segment",
        "Number_of_Customers"
    ]

    st.bar_chart(
        segment_counts,
        x="Segment",
        y="Number_of_Customers"
    )

    st.dataframe(
        segment_counts,
        use_container_width=True
    )

    st.subheader("Revenue by Customer Segment")

    segment_revenue = (
        segments.groupby("Segment")["Monetary"]
        .sum()
        .reset_index()
    )

    segment_revenue.columns = [
        "Segment",
        "Total_Revenue"
    ]

    st.bar_chart(
        segment_revenue,
        x="Segment",
        y="Total_Revenue"
    )

    st.dataframe(
        segment_revenue,
        use_container_width=True
    )

    # Sales Forecasting
elif page == "Sales Forecasting":

    st.header("Sales Forecasting")

    forecast = pd.read_csv(
        "reports/sales_forecast.csv",
        parse_dates=["Month"]
    )

    st.subheader("Predicted Monthly Revenue")

    forecast["Month"] = pd.to_datetime(forecast["Month"])

    forecast["Month_Label"] = forecast["Month"].dt.strftime("%b %Y")

    st.line_chart(
        forecast,
        x="Month_Label",
        y="Forecast_Revenue"
    )

    st.subheader("Forecast Values")

    st.dataframe(
        forecast[["Month", "Forecast_Revenue"]],
        use_container_width=True
    )

    st.info(
        "Note: These revenue forecasts are experimental estimates "
        "based on 12 complete months of historical sales data. "
        "They should not be treated as guaranteed future revenue."
    )