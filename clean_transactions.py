import pandas as pd

df = pd.read_csv(
    "data/raw/investor_transactions.csv",
    sep="\t"
)

# Fix date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Validate amount > 0
invalid_amount = df[df["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amount))

df = df[df["amount_inr"] > 0]

# Check KYC values
print("\nUnique KYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nCleaned Transactions Saved")
print("Rows:", len(df))