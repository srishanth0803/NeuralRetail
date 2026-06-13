import pandas as pd 
import numpy as np 
from prophet import Prophet
from sklearn.metrics import mean_squared_error,mean_absolute_percentage_error
import matplotlib.pyplot as plt 


data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")

data["InvoiceDate"]=pd.to_datetime(data["InvoiceDate"])

series=(
    data.groupby(data["InvoiceDate"].dt.date)["Quantity"]
    .sum()
    .reset_index()
)

series.columns=['ds','y']

#Train&Test.... 

train_size=int(len(series)*0.8)

train=series.iloc[:train_size]
test=series.iloc[train_size:]


#Prohpet model... 

model=Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=True

)

model.fit(train)


#Forecast....... 


future=model.make_future_dataframe(periods=len(test))

forecast=model.predict(future)

#Evaluation..... 

# Evaluation


pred = forecast["yhat"].tail(len(test))

rmse = np.sqrt(
    mean_squared_error(
        test["y"],
        pred
    )
)

mape = mean_absolute_percentage_error(
    test["y"],
    pred
)

print("\nRESULTS")
print("RMSE :", rmse)
print("MAPE :", mape)


# Plot Forecast

fig = model.plot(forecast)

plt.title(
    "Prophet Forecast with Weekly + Yearly Seasonality"
)

plt.savefig(
    "src/forecasting/day6/outputs/dual_seasonality_forecast.png"
)

plt.show()

# Components Plot

fig2 = model.plot_components(
    forecast
)

plt.savefig(
    "src/forecasting/day6/outputs/seasonality_components.png"
)

plt.show()