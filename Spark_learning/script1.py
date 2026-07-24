from pyspark.sql import SparkSession 
spark=SparkSession.builder.appName("Spark Cluster")\
    .config("spark.executor.memory","1g")\
    .config("spark.cores.max","4").getOrCreate()
sc=spark.sparkContext
print("Master:",sc.master)
print("Default Parallelism:",sc.defaultParallelism)
df=spark.range(0,10000000,numPartitions=8)
print("Partitions",df.rdd.getNumPartitions())
df.groupBy().sum().show()
input("Press Enter to stop")
spark.stop()

