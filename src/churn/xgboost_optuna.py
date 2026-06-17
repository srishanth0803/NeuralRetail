import pandas as pd
# pyrefly: ignore [missing-import]
import optuna
# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.xgboost

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv(
    "data/churn_features.csv"
)

X = df[
    [
        "Recency",
        "Frequency",
        "Monetary",
        "frequency_decay",
        "recency_cliff"
    ]
]

y = df["churn"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

def objective(trial):

    params = {
        "max_depth":
        trial.suggest_int(
            "max_depth",
            3,
            10
        ),

        "learning_rate":
        trial.suggest_float(
            "learning_rate",
            0.01,
            0.3
        ),

        "n_estimators":
        trial.suggest_int(
            "n_estimators",
            100,
            500
        ),

        "subsample":
        trial.suggest_float(
            "subsample",
            0.6,
            1.0
        )
    }

    model = XGBClassifier(
        **params,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    pred = model.predict_proba(
        X_test
    )[:,1]

    auc = roc_auc_score(
        y_test,
        pred
    )

    return auc

study = optuna.create_study(
    direction="maximize"
)

study.optimize(
    objective,
    n_trials=100
)

print(study.best_params)