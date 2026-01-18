# Q8. Partitions
# Why does Spark use partitions?
# Answer: B. Parallel processing

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q8").getOrCreate()
data = [Row(x=i) for i in range(10)]
df = spark.createDataFrame(data)
print(f"Number of partitions: {df.rdd.getNumPartitions()}")
print("Spark uses partitions for parallel processing.")
spark.stop()
