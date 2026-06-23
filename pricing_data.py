import pandas as pd

df = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

pricing = df[
    [
        "Price",
        "Quantity"
    ]
].copy()

pricing.columns = [
    "price",
    "demand"
]

pricing["promotion"] = 0

pricing["season"] = 1



print(pricing.head())

import numpy as np

pricing["promotion"] = np.random.choice(
    [0,1],
    size=len(pricing),
    p=[0.8,0.2]
)
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

pricing["season"] = (
    df["InvoiceDate"].dt.quarter
)

pricing.to_csv(
    "data/pricing_data.csv",
    index=False
)