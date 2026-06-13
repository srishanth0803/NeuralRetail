import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf

data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")

series=data.groupby("InvoiceDate")["Quantity"].sum()

plot_acf(series,lags=50)

plt.savefig("src/forecasting/day6/outputs/acf.png")

plt.show()

plot_pacf(series,lags=50)

plt.savefig("src/forecasting/day6/outputs/pacf.png")

plt.show()

