import pandas as pd
# pyrefly: ignore [missing-import]
import shap
import matplotlib.pyplot as plt

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

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

model = XGBClassifier()

model.fit(
    X_train,
    y_train
)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

shap.dependence_plot(
    "Recency",
    shap_values,
    X_test,
    show=False
)

plt.savefig(
    "src/churn/day11/dependence_recency.png",
    bbox_inches="tight"
)

print("Dependence Plot Saved")