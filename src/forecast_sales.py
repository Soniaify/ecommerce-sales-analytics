import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
import matplotlib.pyplot as plt

# Load monthly sales data
sales = pd.read_csv("reports/monthly_sales.csv")

# Convert Month column to date format
sales["Month"] = pd.to_datetime(sales["Month"])

# Sort data by month
sales = sales.sort_values("Month")

print("MONTHLY SALES DATA")
print(sales)

print("\nDATA INFORMATION")
print(sales.info())

from sklearn.linear_model import LinearRegression

# Exclude incomplete December 2011
sales = sales[sales["Month"] < "2011-12-01"].copy()

# Create a time index for the model
sales["Month_Number"] = range(len(sales))

# Select input and target
X = sales[["Month_Number"]]
y = sales["Total_Revenue"]

# Train the forecasting model
model = LinearRegression()
model.fit(X, y)

print("\nMODEL TRAINED SUCCESSFULLY")
print("Months used:", len(sales))
print("Average monthly revenue: £{:,.2f}".format(y.mean()))
print("Trend per month: £{:,.2f}".format(model.coef_[0]))

# Create future month numbers
future_months = pd.DataFrame({
    "Month_Number": [12, 13, 14]
})

# Generate revenue predictions
future_months["Forecast_Revenue"] = model.predict(
    future_months[["Month_Number"]]
)

# Assign forecast dates
future_months["Month"] = pd.date_range(
    start="2011-12-01",
    periods=3,
    freq="MS"
)

# Display forecast results
print("\nNEXT 3 MONTHS REVENUE FORECAST")
print(
    future_months[["Month", "Forecast_Revenue"]]
    .to_string(index=False)
)

# Save forecast results
future_months.to_csv(
    "reports/sales_forecast.csv",
    index=False
)

print("\nFORECAST SAVED SUCCESSFULLY")

# MODEL EVALUATION

# Use the first 9 months for training
train_data = sales.iloc[:9]
test_data = sales.iloc[9:]

# Train a temporary model
evaluation_model = LinearRegression()

evaluation_model.fit(
    train_data[["Month_Number"]],
    train_data["Total_Revenue"]
)

# Predict the final 3 months
test_predictions = evaluation_model.predict(
    test_data[["Month_Number"]]
)

# Compare predictions with actual revenue
mae = mean_absolute_error(
    test_data["Total_Revenue"],
    test_predictions
)

rmse = np.sqrt(
    mean_squared_error(
        test_data["Total_Revenue"],
        test_predictions
    )
)

mape = np.mean(
    np.abs(
        (test_data["Total_Revenue"] - test_predictions)
        / test_data["Total_Revenue"]
    )
) * 100

print("\nMODEL EVALUATION RESULTS")
print(f"MAE: £{mae:,.2f}")
print(f"RMSE: £{rmse:,.2f}")
print(f"MAPE: {mape:.2f}%")

# VISUALISE ACTUAL VS PREDICTED REVENUE

plt.figure(figsize=(10, 6))

plt.plot(
    test_data["Month"],
    test_data["Total_Revenue"],
    marker="o",
    label="Actual Revenue"
)

plt.plot(
    test_data["Month"],
    test_predictions,
    marker="o",
    linestyle="--",
    label="Predicted Revenue"
)

plt.title("Actual vs Predicted Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "reports/forecast_evaluation.png",
    dpi=300
)

plt.close()

print("\nFORECAST EVALUATION CHART CREATED SUCCESSFULLY")

# RANDOM FOREST MODEL EVALUATION

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train using the first 9 months
rf_model.fit(
    train_data[["Month_Number"]],
    train_data["Total_Revenue"]
)

# Predict the final 3 months
rf_predictions = rf_model.predict(
    test_data[["Month_Number"]]
)

# Calculate evaluation metrics
rf_mae = mean_absolute_error(
    test_data["Total_Revenue"],
    rf_predictions
)

rf_rmse = np.sqrt(
    mean_squared_error(
        test_data["Total_Revenue"],
        rf_predictions
    )
)

rf_mape = np.mean(
    np.abs(
        (test_data["Total_Revenue"] - rf_predictions)
        / test_data["Total_Revenue"]
    )
) * 100

print("\nRANDOM FOREST EVALUATION")
print(f"MAE: £{rf_mae:,.2f}")
print(f"RMSE: £{rf_rmse:,.2f}")
print(f"MAPE: {rf_mape:.2f}%")