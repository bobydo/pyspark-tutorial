# Q4. DAG purpose
# Why does Spark build a DAG?
# Answer: B. To optimize and plan execution

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master("local").appName("Q4").getOrCreate()
data = [Row(x=1,y=3), Row(x=1,y=20), Row(x=2,y=30)]
df = spark.createDataFrame(data)
df2 = df.filter(df.x > 0).groupBy(df.x).count()
df2.explain()
print("Spark builds a DAG to optimize and plan execution.")
spark.stop()

# RDD = Resilient Distributed Dataset; fault-tolerant, distributed collection of data.
# DAG = Directed Acyclic Graph; nodes go one way only and no loop excution plan

# AdaptiveSparkPlan isFinalPlan=false => Spark may optimize at runtime, Can change number of partitions, Spark ≥ 3 feature
# +- HashAggregate(keys=[x#0L], functions=[count(1)]) => Combines partial counts, Produces final result
#    +- Exchange hashpartitioning(x#0L, 200), ENSURE_REQUIREMENTS, [plan_id=19] => Data is shuffled, Default 200 shuffle partitions, Data moves across CPU cores / executors
#       +- HashAggregate(keys=[x#0L], functions=[partial_count(1)]) => Local aggregation, Runs before shuffle
#          +- Project [x#0L] => Drops column y, Keeps only x (needed for groupBy), Optimization step
#             +- Filter (isnotnull(x#0L) AND (x#0L > 0)) => Applies df.x > 0
#                +- Scan ExistingRDD[x#0L,y#1L] => Reads the DataFrame from memory
