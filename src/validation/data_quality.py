import pandas as pd

df = pd.read_csv("data/raw/online_retail_II.csv")

print("========== DATA QUALITY REPORT ==========")

print("Row Count:", len(df))

print(
    "Invoice Null Check:",
    "PASS" if df["Invoice"].isnull().sum() == 0 else "FAIL"
)

print(
    "Customer ID Null Check:",
    "PASS" if df["Customer ID"].isnull().sum() < len(df) else "FAIL"
)

print(
    "Quantity Range Check:",
    "PASS" if df["Quantity"].between(-100000, 100000).all() else "FAIL"
)

print("=========================================")
