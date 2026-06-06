import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session

spark = (
SparkSession.builder
.appName("NeuralRetail")
.master("local[*]")
.getOrCreate()
)

print("Reading Dataset.......")

# Read Bronze Layer

data = spark.read.csv(
"data/raw/online_retail_II.csv",
header=True,
inferSchema=True
)

print("Initial Rows:", data.count())

# Remove Null Customer IDs

data = data.filter(col("Customer ID").isNotNull())

# Remove Duplicates

data = data.dropDuplicates()

# Remove Invalid Quantities

data = data.filter(col("Quantity") > 0)

# Remove Invalid Prices

data = data.filter(col("Price") > 0)

print("Rows After Cleaning:", data.count())

# Convert Spark DataFrame to Pandas

pdf = data.toPandas()

# Create Silver Folder

os.makedirs("data/silver", exist_ok=True)

# Save as CSV

pdf.to_csv(
"data/silver/online_retail_II.csv",
index=False
)

print("Silver Layer Created Successfully!")
print("Saved at: data/silver/online_retail_II.csv")

spark.stop()
