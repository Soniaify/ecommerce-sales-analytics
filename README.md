# E-commerce Sales Analytics & Forecasting Dashboard

An end-to-end data analytics project that explores e-commerce sales performance, customer purchasing behaviour, customer segmentation, and revenue forecasting through an interactive Streamlit dashboard.

## Project Overview

This project uses the UCI Online Retail dataset to analyse transactional sales data and extract meaningful business insights.

The analysis covers sales performance, product revenue, geographical sales distribution, customer segmentation using RFM analysis, and experimental revenue forecasting.

## Key Features

- **Data Cleaning:** Removed duplicate transactions, cancelled invoices, invalid quantities, and invalid prices.
- **Sales Analysis:** Analysed revenue trends, order volumes, top-performing products, and country performance.
- **Customer Segmentation:** Applied Recency, Frequency, and Monetary (RFM) analysis to group customers into meaningful segments.
- **Revenue Forecasting:** Compared Linear Regression and Random Forest models using historical monthly revenue.
- **Interactive Dashboard:** Built a multi-page Streamlit dashboard for exploring business performance.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- OpenPyXL

## Dataset

**Source:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)

The original dataset contains 541,909 transactions from a UK-based online retailer between December 2010 and December 2011.

## Project Structure

```text
ecommerce-sales-analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── Online Retail.xlsx
│   └── cleaned_online_retail.csv
│
├── reports/
│   ├── monthly_sales.csv
│   ├── top_products.csv
│   ├── country_sales.csv
│   ├── rfm_customer_metrics.csv
│   ├── customer_segments.csv
│   ├── sales_forecast.csv
│   └── visualisation charts
│
└── src/
    ├── explore_data.py
    ├── investigate_data.py
    ├── clean_data.py
    ├── validate_data.py
    ├── sales_analysis.py
    ├── visualize_sales.py
    ├── rfm_analysis.py
    ├── customer_segmentation.py
    ├── visualize_customers.py
    ├── forecast_sales.py
    └── compare_models.py
```

## Key Findings

- Total positive-sales revenue: approximately **£10.64 million**.
- Total orders: **19,960**.
- Unique products: **3,922**.
- Identifiable customers: **4,338**.
- Sales transactions came from 38 countries.
- November 2011 recorded the highest monthly revenue among the complete months analysed.
- Champions represented the highest-value customer segment by revenue.

## Forecasting Limitations

The forecasting models were evaluated using only 12 complete monthly observations, with the final three months held out for testing.

Both models produced relatively high prediction errors. The forecasts are therefore experimental estimates and should not be treated as reliable business projections.

## Data Processing Notes

The original dataset was preserved. Exact duplicate records, cancelled invoices, non-positive quantities, non-positive unit prices, and missing product descriptions were excluded from the cleaned sales dataset.

Returns and cancellations were excluded, so reported revenue represents positive sales transactions rather than net revenue after returns.

Transactions without CustomerID were retained for general sales analysis but excluded from customer-level RFM analysis.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-sales-analytics.git
```

### 2. Navigate into the project

```bash
cd ecommerce-sales-analytics
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Launch the dashboard

```bash
streamlit run app.py
```

## Author

**Sonia Ify**

Computer Science Graduate | Data Science | Machine Learning | AI & Automation | Robotics

GitHub: [Soniaify](https://github.com/Soniaify)