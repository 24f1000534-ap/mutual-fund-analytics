import pandas as pd

df = pd.read_csv(
    "data/raw/nav_history.csv",
    sep="\t"
)

#--- Convert date---
df["date"] = pd.to_datetime(df["date"])

#----- Sort----
df = df.sort_values(
    ["amfi_code", "date"]
)

#---- Remove duplicates-----
df = df.drop_duplicates()

# -----Forward fill NAV within each fund----
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV rows:")
print(len(invalid_nav))

df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Saved")