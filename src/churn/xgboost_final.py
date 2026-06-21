import pandas as pd
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

mlflow.set_experiment(
    "Day10_Churn"
)

with mlflow.start_run():

    model = XGBClassifier(
        max_depth=5,
        learning_rate=0.1,
        n_estimators=300
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

    mlflow.log_metric(
        "AUC_XGBoost",
        auc
    )

    mlflow.xgboost.log_model(
        model,
        "xgboost_model"
    )

    print("AUC:",auc)