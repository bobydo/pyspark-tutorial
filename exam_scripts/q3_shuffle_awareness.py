# Q3. Shuffle awareness
# Which operation always causes a shuffle?
# A. select()
# B. withColumn()
# C. groupBy()
# D. filter()
# Answer: C. groupBy()

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q3").getOrCreate()
data = [Row(k=1, v=2), Row(k=1, v=3), Row(k=2, v=4)]
df = spark.createDataFrame(data)
# Spark:
# Partitions data by key k
# Shuffles rows across executors; send job to different cpu cores
# Performs the aggregation (count)

grouped = df.groupBy("k").count()
grouped.show()
print("groupBy causes a shuffle in Spark.")

sc = spark.sparkContext
rdd = sc.parallelize([(1, 2), (1, 3), (2, 4)])
# reduceByKey = group by key + add values
result = rdd.reduceByKey(lambda a, b: a + b)
print("reduceByKey causes a shuffle in Spark.", result.collect())

spark.stop()
