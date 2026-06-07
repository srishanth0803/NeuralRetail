import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats 
from statsmodels.tsa.seasonal import seasonal_decompose 


os.makedirs("results/eda",exist_ok=True)

data=pd.read_csv("data/bronze/online_retail_II_bronze.csv")

print("Rows: ",len(data))

print("---------------------------------------------------------------------------------------------")

#Data cleaning

print(data.info())

print("---------------------------------------------------------------------------------------------")

print(data.isnull().sum())

data=data.dropna(subset=["Customer ID"])
data=data[data["Quantity"]>0]
data=data[data["Price"]>0]

#Revenue Column

data["Revenue"]=data["Quantity"]*data["Price"]

#Convert date

data["InvoiceDate"]=pd.to_datetime(data["InvoiceDate"])


print("---------------------------------------------------------------------------------------------")

#1.Revenue Distribution

print("Generating Revenue Distribution...........")

plt.figure(figsize=(12,6))

sns.histplot(data["Revenue"],bins=50,kde=True,color="Red")

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.savefig("results/eda/revenue_distribution.png")

print("Generated Revenue Distribution...")

plt.close()

print("---------------------------------------------------------------------------------------------")

#2.Quantity Distribution

print("Generating Quantity Distribution...........")

plt.figure(figsize=(12,6))

sns.histplot(data["Quantity"],bins=50,kde=True,color="Red")

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.savefig("results/eda/quantity_distribution.png")

print("Generated Quantity Distribution......")

plt.close()

print("---------------------------------------------------------------------------------------------")

#3.Outlier Detection

print("Generating Outlier Detection...........")

plt.figure(figsize=(12,6))

sns.boxplot(x=data["Revenue"],color="Red")
plt.title("Revenue Outlier Detection")
plt.savefig("results/eda/Revenue_Outlier.png")

print("Revenue Outlier Generated.......")


plt.close()


#Z-Score method. 

z_scores = stats.zscore(data["Revenue"])

outliers = data[
    abs(z_scores) > 3
]

print("Outliers Found:", len(outliers))

outliers.to_csv(
    "results/eda/outliers.csv",
    index=False
)

print("---------------------------------------------------------------------------------------------")

#4.Corelation Heatmap...

print("Generating Corelation Heatmap..........")

numeric_cols=data.select_dtypes(include=["float","int"]).columns

corr=data[numeric_cols].corr()

plt.figure(figsize=(12,6))

sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation Heatmap")

plt.savefig("results/eda/correlation_heatmap.png")

print("Correlation Heatmap Generated...........")

plt.close()

print("---------------------------------------------------------------------------------------------")

#5.Seasonality Decomposition..

print("Performing Seasonality Analysis.........")

daily_sales=(
    data.groupby(data["InvoiceDate"].dt.date)["Revenue"].sum().reset_index()
)

daily_sales.columns=["Date","Revenue"]

daily_sales["Date"]=pd.to_datetime(daily_sales["Date"])

daily_sales=daily_sales.set_index("Date")

#Filling Missing Values..

daily_sales = daily_sales.asfreq("D")

daily_sales["Revenue"] = (
    daily_sales["Revenue"]
    .fillna(0)
)

#Seasonal Decompose..

result=seasonal_decompose(
    daily_sales["Revenue"],
    model='additive',period=30
)

fig=result.plot()

fig.set_size_inches(12,8)

fig.savefig("results/eda/seasonality_decomposition.png")

print("Seasonality Analysis Generated.......")

plt.close()

print("---------------------------------------------------------------------------------------------")

#Summary Statistics....

summary=data.describe()

summary.to_csv(
    "results/eda/summary_statistics.csv"
)

print("\nEDA Completed Successfully")
print("Results saved in results/eda/")



