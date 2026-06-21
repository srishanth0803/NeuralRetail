import pandas as pd

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(
    "data/customer_segments.csv"
)

X = df[
    [
        "Recency",
        "Frequency",
        "Monetary"
    ]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(
    eps=0.7,
    min_samples=10
)

labels = dbscan.fit_predict(
    X_scaled
)

df["dbscan_cluster"] = labels

df.to_csv(
    "data/customer_segments_dbscan.csv",
    index=False
)

print(df["dbscan_cluster"].value_counts())