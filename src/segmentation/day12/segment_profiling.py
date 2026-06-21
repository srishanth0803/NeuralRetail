import pandas as pd

df = pd.read_csv(
    "data/customer_segments_gmm.csv"
)

profile = df.groupby(
    "segment"
).agg(

    customers=("segment","count"),

    avg_recency=("Recency","mean"),

    avg_frequency=("Frequency","mean"),

    avg_monetary=("Monetary","mean"),

    churn_rate=("churn","mean")

)

print(profile)

profile.to_csv(
    "reports/segment_profile.csv"
)

print("Profile Saved")

revenue = df.groupby(
    "segment"
)["Monetary"].sum()

print(revenue)

df["CLV"] = (
    df["Frequency"]
    *
    df["Monetary"]
)

clv = df.groupby(
    "segment"
)["CLV"].mean()

print(clv)
