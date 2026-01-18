# Q10. Explain plan
# Why run df.explain(True)?
# Answer: B. View DAG/execution plan

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q10").getOrCreate()
data = [Row(x=i) for i in range(5)]
df = spark.createDataFrame(data)
df2 = df.filter(df.x > 2)
df2.explain(True)
print("df.explain(True) shows the DAG/execution plan.")
spark.stop()
