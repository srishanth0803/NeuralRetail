# pyrefly: ignore [missing-import]
import pandas as pd

rfm = pd.read_csv(
    "data/feature_store/customer_rfm.csv"
)

# Churn Target
rfm["churn"] = (
    rfm["Recency"] > 90
).astype(int)

# Purchase Frequency Decay
rfm["frequency_decay"] = (
    rfm["Frequency"] /
    (rfm["Recency"] + 1)
)

# Recency Cliff
rfm["recency_cliff"] = (
    rfm["Recency"] > 60
).astype(int)

rfm.to_csv(
    "data/churn_features.csv",
    index=False
)

print("Features Created")