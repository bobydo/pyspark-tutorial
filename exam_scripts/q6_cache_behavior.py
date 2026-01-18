# Q6. Cache behavior
# df_cached = df.groupBy("k").count().cache()
# df_cached.show()
# df_cached.count()
# How many times is the aggregation computed?
# A. 0
# B. 1
# C. 2
# D. Depends on cluster
# Answer: B

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q6").getOrCreate()
data = [Row(k=i%2, v=i) for i in range(10)]
df = spark.createDataFrame(data)
df_cached = df.groupBy("k").count().cache()
df_cached.show()  # triggers computation and caches result
df_cached_count = df_cached.count()  # uses cached result, no computation
print(f"Aggregation computed once. Count: {df_cached_count}")
spark.stop()
