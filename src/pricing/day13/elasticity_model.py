import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv(
    "data/pricing_data.csv"
)

# Required columns:
# price
# demand
# promotion
print(df[["price","demand"]].describe())

print(
    "Zero prices:",
    (df["price"] <= 0).sum()
)

print(
    "Zero demand:",
    (df["demand"] <= 0).sum()
)

print(
    df[
        (df["price"] <= 0) |
        (df["demand"] <= 0)
    ].head()
)



# Remove invalid rows

df = df[
    (df["price"] > 0) &
    (df["demand"] > 0)
]

# Log Transform

df["log_price"] = np.log(
    df["price"]
)

df["log_demand"] = np.log(
    df["demand"]
)

X = df[
    [
        "log_price",
        "promotion"
    ]
]

X = sm.add_constant(X)

y = df["log_demand"]


model = sm.OLS(
    y,
    X
).fit()

print(model.summary())

elasticity = model.params["log_price"]

print(
    "\nPrice Elasticity:",
    elasticity
)

model.summary().as_csv()

with open(
    "reports/elasticity_report.csv",
    "w"
) as f:

    f.write(
        model.summary().as_csv()
    )
    