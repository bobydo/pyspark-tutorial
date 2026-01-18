# Q9. Execution order
# df.filter(...).groupBy("k").count()
# Which executes first?
# Answer: C. Optimized together

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q9").getOrCreate()
data = [Row(k=i%2, v=i) for i in range(10)]
df = spark.createDataFrame(data)
result = df.filter(df.v > 2).groupBy("k").count()
result.explain(True)
print("Spark optimizes the execution plan, so operations are optimized together.")
spark.stop()
