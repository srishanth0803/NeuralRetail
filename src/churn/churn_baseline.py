
from numpy.matlib import rand
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import roc_auc_score,f1_score,confusion_matrix

import matplotlib.pyplot as plt 
# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.sklearn


rfm=pd.read_csv("data/feature_store/customer_rfm.csv")

#create churn label.. 

rfm["Churn"]=(rfm["Recency"]>90).astype(int)

X=rfm[
    [
        "Recency",
        "Frequency",
        "Monetary"
    ]
]

y=rfm["Churn"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

mlflow.set_experiment("Customer Churn")

with mlflow.start_run():

    model=LogisticRegression()

    model.fit(
        X_train,y_train
    )

    pred=model.predict(X_test)

    prob=model.predict_proba(X_test)[:,1]

    auc=roc_auc_score(y_test,prob)

    f1=f1_score(y_test,pred)

    cm=confusion_matrix(y_test,pred)

    plt.imshow(cm)

    plt.savefig("confusion_matrix.png")

    mlflow.log_metric(
        "AUC_ROC",auc
    )

    mlflow.log_metric(
        "f1",f1
    )

    mlflow.log_artifact(
        "confusion_matrix.png"
    )
    mlflow.sklearn.log_model(
        model,"logistic_model"
    )

    print("AUC: ",auc)
    print("f1: ",f1)

