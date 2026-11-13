import pandas as pd

# Model comparison results
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest"
    ],
    "MAE": [
        502050.35,
        486086.43
    ],
    "RMSE": [
        536049.40,
        522816.79
    ],
    "MAPE": [
        39.28,
        37.91
    ]
})

# Save comparison report
results.to_csv(
    "reports/model_comparison.csv",
    index=False
)

print("MODEL COMPARISON REPORT CREATED")
print(results.to_string(index=False))