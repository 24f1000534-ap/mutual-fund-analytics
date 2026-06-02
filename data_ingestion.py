import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print(f"\nTotal CSV files found: {len(csv_files)}")

for file in csv_files:

    path = os.path.join(folder_path, file)

    print("\n" + "="*70)
    print("FILE:", file)

    try:
        df = pd.read_csv(path , sep="\t")

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())

    except Exception as e:
        print("Error:", e)