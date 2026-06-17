import numpy as np
# pyrefly: ignore [missing-import]
import mlflow

from sklearn.metrics import mean_absolute_percentage_error

actual = np.array([100,120,140,160,180])

prophet_pred = np.array([102,122,138,165,178])

lstm_pred = np.array([98,118,145,158,182])

BEST_WEIGHT = 0.65

ensemble_pred = (
    BEST_WEIGHT * prophet_pred +
    (1-BEST_WEIGHT) * lstm_pred
)

mape = mean_absolute_percentage_error(
    actual,
    ensemble_pred
)

mlflow.set_experiment(
    "Demand Forecast Comparison"
)

with mlflow.start_run(
    run_name="Prophet_LSTM_Ensemble"
):

    mlflow.log_metric(
        "MAPE_Ensemble",
        mape
    )

    mlflow.log_param(
        "Prophet_Weight",
        BEST_WEIGHT
    )

    mlflow.log_param(
        "LSTM_Weight",
        1-BEST_WEIGHT
    )

print("Ensemble MAPE:",mape)


