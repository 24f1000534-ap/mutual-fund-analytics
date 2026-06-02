import requests
import pandas as pd

schemes = {
    "125497": "HDFC_Top100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_LargeCap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

for code, name in schemes.items():

    print(f"\nFetching {name} ({code})")

    try:

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        print("Status Code:", response.status_code)

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{name}_live_nav.csv",
            index=False
        )

        print(f"{name} saved")

    except Exception as e:

        print(f"ERROR for {name}")
        print(e)

        print("\nResponse Text:")
        print(response.text[:500])