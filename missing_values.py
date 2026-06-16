import pandas as pd 

data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")

print("Missing values: ",data.isnull().sum())


print("Before:", len(data))

data = data.dropna(subset=["Customer ID"])

print("After:", len(data))
