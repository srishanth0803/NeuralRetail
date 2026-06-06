from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder\
    .appName("NeyralRetail-EDA")\
    .getOrCreate()

data=spark.read.csv("data/silver/online_retail_II",header=True,inferSchema=True)

data=data.withColumn("Revenue",col("Quantity")*col("Price"))

print("-----------------------------------------------------------------------------------")

print("Dataset Summary")

print("-----------------------------------------------------------------------------------")

print("Total Rows: ",data.count())

print("Total Customers: ",data.select("Customer ID").distint().count())

print("Total Products: ",data.select("Stockcode").distint().count())

print("Total Countries: ",data.select("Country").distint().count())


print("=" * 50)
print("TOP 10 PRODUCTS")
print("=" * 50)

data.groupBy("Description") \
    .agg(sum("Quantity").alias("UnitsSold")) \
    .orderBy(desc("UnitsSold")) \
    .show(10, False)

print("=" * 50)
print("TOP COUNTRIES BY REVENUE")
print("=" * 50)

data.groupBy("Country") \
    .agg(
        round(sum("Revenue"), 2).alias("Revenue")
    ) \
    .orderBy(desc("Revenue")) \
    .show(10, False)

spark.stop()