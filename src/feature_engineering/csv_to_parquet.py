import pandas as pd
import os

os.makedirs("feature_repo/feature_repo/data", exist_ok=True)

# ==========================
# Customer RFM
# ==========================

rfm = pd.read_csv(
    "data/feature_store/customer_rfm.csv"
)

rfm["event_timestamp"] = pd.Timestamp.now()

rfm.to_parquet(
    "feature_repo/feature_repo/data/customer_rfm.parquet",
    index=False
)

print("customer_rfm.parquet created")

# ==========================
# Demand Features
# ==========================

demand = pd.read_csv(
    "data/feature_store/demand_features.csv",
    low_memory=False
)

# Convert mixed-type columns

demand["StockCode"] = demand["StockCode"].astype(str)

demand["event_timestamp"] = pd.Timestamp.now()

demand.to_parquet(
    "feature_repo/feature_repo/data/demand_features.parquet",
    index=False
)

print("demand_features.parquet created")