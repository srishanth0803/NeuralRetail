import pandas as pd
import numpy as np

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

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

# -------------------
# ADF Test
# -------------------

adf_result = adfuller(series)

print("\nADF TEST")
print("Statistic:", adf_result[0])
print("P-value:", adf_result[1])

# -------------------
# KPSS Test
# -------------------

kpss_result = kpss(series)

print("\nKPSS TEST")
print("Statistic:", kpss_result[0])
print("P-value:", kpss_result[1])

# -------------------
# Log Transform
# -------------------

log_series = np.log1p(series)

# -------------------
# Differencing
# -------------------

diff_series = log_series.diff().dropna()

print("\nDifferenced Series")
print(diff_series.head())

# Save
diff_series.to_csv(
    "src/forecasting/day6/outputs/differenced_series.csv"
)

print(
    "\nSaved: src/forecasting/day6/outputs/differenced_series.csv"
)