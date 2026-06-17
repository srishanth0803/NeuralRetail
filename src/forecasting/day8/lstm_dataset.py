import pandas as pd
import numpy as np

data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

series = (
    data.groupby("InvoiceDate")["Quantity"]
    .sum()
    .reset_index()
)

values = series["Quantity"].values
LOOKBACK = 28

X = []
y = []

for i in range(len(values)-LOOKBACK-30):

    X.append(values[i:i+LOOKBACK])

    y.append([
        values[i+LOOKBACK],
        values[i+LOOKBACK+6],
        values[i+LOOKBACK+29]
    ])

X = np.array(X)
y = np.array(y)

print(X.shape)
print(y.shape)