import pandas as pd

nav=pd.read_csv("data/raw/nav_history.csv",sep="\t")

print("columns:")
print(nav.columns)

print("\n First5 rows:")
print(nav.head())