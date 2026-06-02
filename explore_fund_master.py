import pandas as pd

df = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

print("\nTOTAL SCHEMES:")
print(df.shape[0])

print("\nTOTAL FUND HOUSES:")
print(df["fund_house"].nunique())

print("\nFUND HOUSES:")
print(df["fund_house"].unique())

print("\nCATEGORIES:")
print(df["category"].unique())

print("\nSUB CATEGORIES:")
print(df["sub_category"].unique())

print("\nRISK CATEGORIES:")
print(df["risk_category"].unique())