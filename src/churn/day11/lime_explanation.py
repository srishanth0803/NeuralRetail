import pandas as pd

# pyrefly: ignore [missing-import]
from lime.lime_tabular import LimeTabularExplainer

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

explainer = LimeTabularExplainer(
    training_data=X_train.values,
    feature_names=X.columns,
    class_names=["No Churn","Churn"],
    mode="classification"
)

exp = explainer.explain_instance(
    X_test.iloc[0].values,
    model.predict_proba,
    num_features=5
)

exp.save_to_file(
    "src/churn/day11/lime_explanation.html"
)

print("LIME Saved")