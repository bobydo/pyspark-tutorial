# Q1. Lazy execution
# What happens when this code runs?
# df2 = df.filter(df.x > 10).select("x")

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q1").getOrCreate()
data = [Row(x=5), Row(x=11), Row(x=15)]
df = spark.createDataFrame(data)
df2 = df.filter(df.x > 10).select("x")
print("DataFrame transformations are lazy. No execution yet.")
print("DAG is built, but not executed until an action is called.")
print("\nNow calling an action: df2.show()\n")
df2.show()  # This triggers execution
print("\nNow calling an action: df.collect()\n")
collected = df.collect() # This triggers execution
print("Result of df.collect():", collected)
print("Result of df.collect():")
for row in collected:
    print(row)
count = df2.count()
print(f"Action 'count()' triggers execution. Count: {count}")
spark.stop()
