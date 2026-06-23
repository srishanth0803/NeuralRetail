import pandas as pd

df = pd.read_csv(
    "data/pricing_data.csv"
)

promo = df[
    df["promotion"] == 1
]

nonpromo = df[
    df["promotion"] == 0
]

promo_sales = promo["demand"].mean()

normal_sales = nonpromo["demand"].mean()

lift = (

    (
        promo_sales
        -
        normal_sales
    )
    /
    normal_sales

) * 100

print(
    "Promotion Lift:",
    round(lift,2),
    "%"
)