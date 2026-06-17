import pandas as pd
# pyrefly: ignore [missing-import]
import mlflow

# pyrefly: ignore [missing-import]
from neuralprophet import NeuralProphet
from sklearn.metrics import mean_absolute_percentage_error

data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"]
)

daily = (
    data.groupby("InvoiceDate")
    ["Quantity"]
    .sum()
    .reset_index()
)

daily.columns = [
    "ds",
    "y"
]

model = NeuralProphet(
    learning_rate=0.01
)


metrics = model.fit(
    daily,
    freq="D"
)

future = model.make_future_dataframe(
    daily,
    periods=30
)

forecast = model.predict(
    future
)

forecast.to_csv(
    "src/forecasting/day9/outputs/neuralprophet_forecast.csv",
    index=False
)

actual = daily["y"].tail(30)

pred = forecast["yhat1"].tail(30)

mape = mean_absolute_percentage_error(
    actual,
    pred
)

mlflow.set_experiment(
    "Demand Forecast Comparison"
)

with mlflow.start_run(
    run_name="NeuralProphet"
):

    mlflow.log_metric(
        "MAPE_NeuralProphet",
        mape
    )

print("NeuralProphet MAPE:",mape)