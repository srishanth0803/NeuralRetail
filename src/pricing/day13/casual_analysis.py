import pandas as pd

# pyrefly: ignore [missing-import]
from dowhy import CausalModel

df = pd.read_csv(
    "data/pricing_data.csv"
)

model = CausalModel(

    data=df,

    treatment="price",

    outcome="demand",

    common_causes=[
        "promotion",
        "season"
    ]
)

identified_estimand = model.identify_effect()

estimate = model.estimate_effect(

    identified_estimand,

    method_name="backdoor.linear_regression"
)

print(
    estimate
)
