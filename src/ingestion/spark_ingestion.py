# pyrefly: ignore [missing-import]
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NeuralRetail") \
    .getOrCreate()

print("Reading dataset...")

data = spark.read.csv(
    "data/raw/online_retail_II.csv",
    header=True,
    inferSchema=True
)

print("Rows:", data.count())
print("Columns:", len(data.columns))

# Convert Spark DataFrame to Pandas
pdf = data.toPandas()

# Save Bronze Layer
pdf.to_csv(
    "data/bronze/online_retail_II_bronze.csv",
    index=False
)

print("Bronze layer created")