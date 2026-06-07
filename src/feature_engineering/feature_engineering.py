import pandas as pd
import numpy as np
import holidays
import requests
import os

print("Loading dataset...")

# =====================================================
# LOAD DATA
# =====================================================

data = pd.read_csv(
    "data/bronze/online_retail_II_bronze.csv"
)

# =====================================================
# DATE CONVERSION
# =====================================================

data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

# Revenue Feature
data["Revenue"] = data["Quantity"] * data["Price"]

# =====================================================
# DATE FEATURES
# =====================================================

print("Creating date features...")

data["day_of_week"] = data["InvoiceDate"].dt.dayofweek
data["week_of_year"] = data["InvoiceDate"].dt.isocalendar().week
data["month"] = data["InvoiceDate"].dt.month
data["quarter"] = data["InvoiceDate"].dt.quarter
data["year"] = data["InvoiceDate"].dt.year

data["is_weekend"] = np.where(
    data["day_of_week"] >= 5,
    1,
    0
)

# =====================================================
# HOLIDAY FLAGS
# =====================================================

print("Adding holiday flags...")

uk_holidays = holidays.UK()

data["holiday_flag"] = data["InvoiceDate"].dt.date.apply(
    lambda x: 1 if x in uk_holidays else 0
)

# =====================================================
# PROMOTION FLAGS
# =====================================================

print("Creating promo flags...")

data["promo_flag"] = 0

data.loc[
    data["month"].isin([11, 12]),
    "promo_flag"
] = 1

# =====================================================
# DAILY DEMAND FEATURES
# =====================================================

print("Creating daily demand dataset...")

daily = (
    data.groupby(
        [
            "StockCode",
            pd.Grouper(
                key="InvoiceDate",
                freq="D"
            )
        ]
    )["Quantity"]
    .sum()
    .reset_index()
)

daily = daily.sort_values(
    ["StockCode", "InvoiceDate"]
)

# =====================================================
# LAG FEATURES
# =====================================================

print("Creating lag features...")

daily["lag_1"] = (
    daily.groupby("StockCode")["Quantity"]
    .shift(1)
)

daily["lag_7"] = (
    daily.groupby("StockCode")["Quantity"]
    .shift(7)
)

daily["lag_14"] = (
    daily.groupby("StockCode")["Quantity"]
    .shift(14)
)

# =====================================================
# ROLLING MEAN FEATURES
# =====================================================

print("Creating rolling means...")

daily["rolling_mean_7"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(7).mean()
    )
)

daily["rolling_mean_14"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(14).mean()
    )
)

daily["rolling_mean_30"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(30).mean()
    )
)

# =====================================================
# ROLLING STD FEATURES
# =====================================================

print("Creating rolling std features...")

daily["rolling_std_7"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(7).std()
    )
)

daily["rolling_std_14"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(14).std()
    )
)

daily["rolling_std_30"] = (
    daily.groupby("StockCode")["Quantity"]
    .transform(
        lambda x: x.rolling(30).std()
    )
)

# =====================================================
# RFM ANALYSIS
# =====================================================

print("Calculating RFM scores...")

snapshot_date = (
    data["InvoiceDate"].max()
    + pd.Timedelta(days=1)
)

rfm = (
    data.groupby("Customer ID")
    .agg(
        {
            "InvoiceDate": lambda x:
            (snapshot_date - x.max()).days,

            "Invoice": "count",

            "Revenue": "sum"
        }
    )
)

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

rfm["R_score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)

rfm["F_score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["M_score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["RFM_Score"] = (
    rfm["R_score"].astype(str)
    + rfm["F_score"].astype(str)
    + rfm["M_score"].astype(str)
)

# =====================================================
# WEATHER DATA
# =====================================================

print("Downloading weather data...")

weather_data = pd.DataFrame()

try:

    weather_url = (
        "https://archive-api.open-meteo.com/v1/archive"
        "?latitude=51.5074"
        "&longitude=-0.1278"
        "&start_date=2009-01-01"
        "&end_date=2011-12-31"
        "&daily=temperature_2m_mean"
        "&timezone=auto"
    )

    weather = requests.get(
        weather_url,
        timeout=20
    ).json()

    weather_data = pd.DataFrame(
        {
            "InvoiceDate":
            pd.to_datetime(
                weather["daily"]["time"]
            ),

            "temperature":
            weather["daily"][
                "temperature_2m_mean"
            ]
        }
    )

except Exception as e:

    print("Weather API failed:", e)

# =====================================================
# CPI DATA
# =====================================================

print("Creating CPI feature...")

cpi = pd.DataFrame(
    {
        "year": [2009, 2010, 2011],
        "CPI": [100, 103, 106]
    }
)

data = data.merge(
    cpi,
    on="year",
    how="left"
)

# =====================================================
# WEATHER JOIN
# =====================================================

if len(weather_data) > 0:

    data["InvoiceDate"] = data["InvoiceDate"].dt.normalize()

    data = data.merge(
        weather_data,
        on="InvoiceDate",
        how="left"
    )

# =====================================================
# CREATE OUTPUT FOLDER
# =====================================================

os.makedirs(
    "data/feature_store",
    exist_ok=True
)

# =====================================================
# SAVE OUTPUTS
# =====================================================

print("Saving files...")

data.to_parquet(
    "data/feature_store/retail_features.parquet",
    index=False
)

rfm.to_csv(
    "data/feature_store/customer_rfm.csv"
)

daily.to_csv(
    "data/feature_store/demand_features.csv",
    index=False
)

print("\n================================")
print("FEATURE ENGINEERING COMPLETED")
print("================================")

print("Saved:")
print("1. customer_rfm.csv")
print("2. demand_features.csv")
print("3. retail_features.parquet")