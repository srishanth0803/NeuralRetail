import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    max,
    sum,
    count,
    datediff,
    current_date
)

spark = (
    SparkSession.builder
    .appName("NeuralRetail-Gold")
    .master("local[*]")
    .getOrCreate()
)

print("Reading Silver Layer...")

df = spark.read.csv(
    "data/silver/online_retail_II.csv",
    header=True,
    inferSchema=True
)

# Revenue Column
df = df.withColumn(
    "Revenue",
    col("Quantity") * col("Price")
)

# RFM Calculation
rfm = df.groupBy("Customer ID").agg(
    datediff(
        current_date(),
        max("InvoiceDate")
    ).alias("Recency"),

    count("Invoice").alias("Frequency"),

    sum("Revenue").alias("Monetary")
)

print("Customers:", rfm.count())

# Convert Spark DataFrame to Pandas
rfm_pd = rfm.toPandas()

# Create Gold Folder
os.makedirs("data/gold", exist_ok=True)

# Save CSV
rfm_pd.to_csv(
    "data/gold/customer_rfm.csv",
    index=False
)

print("Gold Layer Created Successfully!")
print("Saved at data/gold/customer_rfm.csv")

spark.stop()