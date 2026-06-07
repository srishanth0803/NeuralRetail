from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("NeuralRetail-Delta")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet(
    "data/feature_store/retail_features.parquet"
)

df.write.format("delta") \
    .mode("overwrite") \
    .save("data/delta/retail_features")

print("Delta Table Created")

spark.stop()