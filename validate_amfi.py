import pandas as pd

fund_master = pd.read_csv(
    "data/raw/fund_master.csv",
    sep="\t"
)

nav_history = pd.read_csv(
    "data/raw/nav_history.csv",
    sep="\t"
)

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Total schemes in fund_master:",
      len(fund_codes))

print("Total schemes in nav_history:",
      len(nav_codes))

print("Missing AMFI codes:",
      len(missing_codes))

print("\nMissing Code List:")
print(missing_codes)