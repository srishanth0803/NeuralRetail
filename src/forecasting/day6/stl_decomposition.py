import pandas as pd
import numpy as np

from statsmodels.tsa.seasonal import STL

import matplotlib.pyplot as plt


# Load data
data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

# Convert date column
data["InvoiceDate"] = pd.to_datetime(
    data["InvoiceDate"]
)

# Create daily demand series
series = (
    data.groupby("InvoiceDate")["Quantity"]
    .sum()
    .sort_index()
)

stl=STL(series,period=7)

result=stl.fit()
result.plot()

plt.savefig(
     "src/forecasting/day6/outputs/stl_decomposition.png"
)

plt.show()

