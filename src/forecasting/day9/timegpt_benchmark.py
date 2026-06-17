import pandas as pd
# pyrefly: ignore [missing-import]
import mlflow

# pyrefly: ignore [missing-import]
from nixtla import NixtlaClient
from sklearn.metrics import mean_absolute_percentage_error

client = NixtlaClient(
    api_key="nixak-74b61e295685c4323c2e75fe88c4a1f5600506cd53d31157cbc143bf508592256398614de20038e9"
)

import pandas as pd

data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"]
)

daily = (
    data.groupby(
        pd.Grouper(
            key="InvoiceDate",
            freq="D"
        )
    )["Quantity"]
    .sum()
    .reset_index()
)

daily.columns = ["ds", "y"]

daily = daily.sort_values("ds")

print(daily.head())
