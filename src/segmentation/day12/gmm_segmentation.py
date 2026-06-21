import pandas as pd

from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(
    "data/customer_segments_dbscan.csv"
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

gmm = GaussianMixture(
    n_components=6,
    random_state=42
)

gmm.fit(
    X_scaled
)

df["gmm_segment"] = gmm.predict(
    X_scaled
)

df["segment_probability"] = gmm.predict_proba(
    X_scaled
).max(axis=1)

df.to_csv(
    "data/customer_segments_gmm.csv",
    index=False
)

print("GMM Completed")