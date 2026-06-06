import pandas as pd

df = pd.read_csv("data/raw/online_retail_II.csv")

print("Total Rows:", len(df))

print(
    "Invoice Null Check:",
    df["Invoice"].isnull().sum() == 0
)

print(
    "Quantity Range Check:",
    df["Quantity"].between(-100000, 100000).all()
)