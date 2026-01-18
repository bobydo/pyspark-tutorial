# Q1. Predicate Pushdown
# You run the following code:
# df = spark.read.parquet("data").filter("x > 10")
# What optimization may occur?
# A. Spark reads all rows, then filters in memory
# B. Spark applies the filter during data read
# C. Spark disables caching
# D. Spark increases shuffle partitions
# ✅ Answer: B


import sys
import os
from pyspark.sql import SparkSession
from pyspark.sql import Row

print("HADOOP_HOME:", os.environ.get("HADOOP_HOME"))
print("PATH:", os.environ.get("PATH"))

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from setup_pyspark_env import setup_pyspark_env
# setup_pyspark_env()

spark = (
    SparkSession.builder
    .master("local[1]")   # 👈 IMPORTANT: NOT local[*]
    .appName("ParquetPushdownDemo")
    .config("spark.sql.execution.arrow.pyspark.enabled", "false")
    .config("spark.python.worker.reuse", "false")
    .getOrCreate()
)

data = [
    Row(id=1, x=5),
    Row(id=2, x=15),
    Row(id=3, x=25),
    Row(id=4, x=8)
]

df = spark.createDataFrame(data)
df.write.mode("overwrite").parquet("parquet_data")
df_filtered = spark.read.parquet("parquet_data") \
    .filter("x > 10")
df_filtered.explain(True)
df_filtered.show()
