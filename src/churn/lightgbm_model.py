import pandas as pd
# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.lightgbm

from lightgbm import LGBMClassifier
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
# pyrefly: ignore [missing-import]
from imblearn.over_sampling import SMOTE

smote = SMOTE(
    random_state=42
)



X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
X_train,y_train = smote.fit_resample(
    X_train,
    y_train
)

with mlflow.start_run():

    model = LGBMClassifier(
        boosting_type="dart"
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
        "AUC_LightGBM",
        auc
    )

    mlflow.lightgbm.log_model(
        model,
        "lightgbm_model"
    )

    print("AUC:",auc)