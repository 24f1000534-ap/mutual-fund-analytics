import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

datasets = [
    "fund_master.csv",
    "portfolio_holdings.csv",
    "aum_by_fund_house.csv",
    "benchmark_indices.csv",
    "category_inflows.csv",
    "industry_folio_count.csv",
    "monthly_sip_inflows.csv"
]

for file in datasets:

    print(f"\nProcessing {file}")

    df = pd.read_csv(
        os.path.join(raw_path, file),
        sep="\t"
    )

    before = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date columns if present
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(
                    df[col],
                    errors="ignore"
                )
            except:
                pass

    after = len(df)

    output_file = file.replace(
        ".csv",
        "_clean.csv"
    )

    df.to_csv(
        os.path.join(processed_path, output_file),
        index=False
    )

    print(
        f"Rows: {before} -> {after}"
    )

print("\nAll datasets cleaned successfully.")