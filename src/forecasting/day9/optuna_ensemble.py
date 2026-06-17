import numpy as np
# pyrefly: ignore [missing-import]
import optuna

from sklearn.metrics import mean_absolute_percentage_error

actual = np.array([100,120,140,160,180])

prophet_pred = np.array([102,122,138,165,178])

lstm_pred = np.array([98,118,145,158,182])

def objective(trial):

    prophet_weight = trial.suggest_float(
        "prophet_weight",
        0,
        1
    )

    ensemble = (
        prophet_weight * prophet_pred +
        (1-prophet_weight) * lstm_pred
    )

    mape = mean_absolute_percentage_error(
        actual,
        ensemble
    )

    return mape

study = optuna.create_study(
    direction="minimize"
)

study.optimize(
    objective,
    n_trials=50
)

print("\nBest Weight")
print(study.best_params)

print("\nBest MAPE")
print(study.best_value)


