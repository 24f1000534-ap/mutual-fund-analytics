import pandas as pd

df = pd.read_csv(
    "data/raw/scheme_performance.csv",
    sep="\t"
)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check for non-numeric values
print("Missing values after conversion:")
print(df[return_cols].isna().sum())

# Flag anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nReturn Anomalies:", len(anomalies))

# Validate expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Issues:", len(invalid_expense))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nCleaned Performance File Saved")
print("Rows:", len(df))