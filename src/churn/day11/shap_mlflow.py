# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.sklearn

import pandas as pd

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv("data/churn_features.csv")

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

mlflow.set_experiment(
    "Day11_SHAP"
)

with mlflow.start_run():

    model = XGBClassifier()

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

    mlflow.log_metric(
        "AUC",
        auc
    )

    mlflow.log_artifact(
        "src/churn/day11/shap_summary.png"
    )

    mlflow.log_artifact(
        "src/churn/day11/shap_beeswarm.png"
    )

    mlflow.log_artifact(
        "src/churn/day11/waterfall_customer_1.png"
    )

    mlflow.log_artifact(
        "src/churn/day11/dependence_recency.png"
    )

    mlflow.sklearn.log_model(
        model,
        "xgb_shap_model"
    )

    print("Logged to MLflow")