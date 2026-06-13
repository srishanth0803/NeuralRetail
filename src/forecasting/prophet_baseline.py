import pandas as pd 
import numpy as np 

from prophet import Prophet

from sklearn.metrics import(mean_absolute_error,mean_absolute_percentage_error)

# pyrefly: ignore [missing-import]
import mlflow
# pyrefly: ignore [missing-import]
import mlflow.prophet

data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")

data["InvoiceDate"]=pd.to_datetime(data["InvoiceDate"])

daily=(data.groupby("InvoiceDate")["Quantity"].sum().reset_index())

daily.columns=["ds","y"]

train_size=int(len(daily)*0.8)

train=daily[:train_size]

test=daily[train_size:]

#MLflow... 

mlflow.set_experiment("Demand Forecasting..")

with mlflow.start_run():
    model=Prophet()
    model.fit(train)
    future=model.make_future_dataframe(periods=len(test))
    forecast=model.predict(future)
    pred=forecast['yhat'].tail(len(test))
    rmse=np.sqrt(mean_absolute_error(test['y'],pred))
    mape=mean_absolute_percentage_error(test['y'],pred)
    mlflow.log_metric(
        "RMSE",rmse
    )
    mlflow.log_metric(
        "MAPE",mape
    )
    mlflow.prophet.log_model(
        model,"prohpet_model"
    )
    print("RMSE: ",rmse)
    print("MAPE: ",mape)

    


