# Q5. Performance issue
# Poor performance after groupBy is most likely due to:
# Answer: B. Shuffle and data movement

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q5").getOrCreate()
data = [Row(k=i%2, v=i) for i in range(100)]
df = spark.createDataFrame(data)
grouped = df.groupBy("k").count()
grouped.show()
print("Performance issue is likely due to shuffle and data movement.")
spark.stop()
