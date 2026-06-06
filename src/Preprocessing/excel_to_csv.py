import pandas as pd

df = pd.read_excel(
    "data/raw/online_retail_II.xlsx"
)

df.to_csv(
    "data/raw/online_retail_II.csv",
    index=False
)

print("CSV created successfully")
