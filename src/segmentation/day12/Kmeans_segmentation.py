import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score
)

df = pd.read_csv(
    "data/churn_features.csv"
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

# -------------------
# Elbow Method
# -------------------

wcss = []

for k in range(2,11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    wcss.append(
        model.inertia_
    )

plt.figure(figsize=(8,5))

plt.plot(
    range(2,11),
    wcss,
    marker="o"
)

plt.xlabel("Clusters")

plt.ylabel("WCSS")

plt.title("Elbow Method")

plt.savefig(
    "src/segmentation/day12/elbow_curve.png"
)

# -------------------
# Silhouette Scores
# -------------------

for k in range(2,11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(
        X_scaled
    )

    sil = silhouette_score(
        X_scaled,
        labels
    )

    db = davies_bouldin_score(
        X_scaled,
        labels
    )

    print(
        f"K={k} | Silhouette={sil:.4f} | DB={db:.4f}"
    )

# Final k = 6

model = KMeans(
    n_clusters=6,
    random_state=42,
    n_init=10
)

df["segment"] = model.fit_predict(
    X_scaled
)

df.to_csv(
    "data/customer_segments.csv",
    index=False
)

print("Segments Saved")