import pandas as pd
import numpy as np

import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

# pyrefly: ignore [missing-import]
import pytorch_lightning as pl

# pyrefly: ignore [missing-import]
import mlflow

# pyrefly: ignore [missing-import]
from lstm_model import LSTMForecast

data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"]
)

series = (
    data.groupby("InvoiceDate")["Quantity"]
    .sum()
)

values = series.values

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
X = torch.tensor(
    X,
    dtype=torch.float32
).unsqueeze(-1)

y = torch.tensor(
    y,
    dtype=torch.float32
)

dataset = TensorDataset(X,y)

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

mlflow.set_experiment(
    "LSTM Demand Forecast"
)

mlflow.pytorch.autolog()

with mlflow.start_run():

    model = LSTMForecast()

    trainer = pl.Trainer(
        max_epochs=20,
        gradient_clip_val=1.0
    )

    trainer.fit(
        model,
        loader
    )
    mlflow.set_experiment(
    "Demand Forecast Comparison"
)

with mlflow.start_run(
    run_name="LSTM"
):
    mlflow.log_metric(
        "MAPE_LSTM",
        # pyrefly: ignore [unknown-name]
        mape
    )