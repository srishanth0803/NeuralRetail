import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

from sklearn.metrics import (
    roc_auc_score,
    classification_report
)

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

base_models = [

    (
        "xgb",
        XGBClassifier(
            eval_metric="logloss"
        )
    ),

    (
        "lgbm",
        LGBMClassifier()
    ),

    (
        "rf",
        RandomForestClassifier()
    )
]

stack = StackingClassifier(

    estimators=base_models,

    final_estimator=
    LogisticRegression()
)

stack.fit(
    X_train,
    y_train
)

# Probabilities
prob = stack.predict_proba(
    X_test
)[:, 1]

auc = roc_auc_score(
    y_test,
    prob
)

print(
    "Stacking AUC:",
    auc
)

# Threshold = 0.35
pred = (
    prob > 0.35
).astype(int)

print(
    classification_report(
        y_test,
        pred
    )
)