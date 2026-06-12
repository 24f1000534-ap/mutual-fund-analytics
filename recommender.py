import pandas as pd

df = pd.read_csv("../data/processed/scheme_performance_clean.csv")

risk_mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}

risk_appetite = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

filtered = df[
    df["risk_grade"].isin(
        risk_mapping[risk_appetite]
    )
]

recommendations = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)