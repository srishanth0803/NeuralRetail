import pandas as pd
import numpy as np

# pyrefly: ignore [missing-import]
from econml.dml import LinearDML

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(
    "data/pricing_data.csv"
)

Y = df["demand"]

T = df["price"]

X = df[
    [
        "promotion",
        "season"
    ]
]

dml = LinearDML(

    model_y=
    RandomForestRegressor(),

    model_t=
    RandomForestRegressor(),

    random_state=42
)

dml.fit(

    Y,

    T,

    X=X
)

effects = dml.effect(
    X
)

print(
    effects[:10]
)