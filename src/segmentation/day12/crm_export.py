import pandas as pd

df = pd.read_csv(
    "data/customer_segments_gmm.csv"
)

high_risk = df[
    (df["churn"]==1)
]

high_risk["retention_action"] = (
    "OFFER_DISCOUNT"
)

high_risk[
    [
        "Customer ID",
        "segment",
        "retention_action"
    ]
].to_csv(

    "reports/high_risk_customers.csv",

    index=False
)

print("CRM Export Saved")