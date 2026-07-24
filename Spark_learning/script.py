from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("Spark Learning").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
data=[("Alice", 34), ("Bob", 45), ("Charlie", 29)]
columns=["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()
input("open http://localhost:4040 in your browser to see the Spark UI. Press Enter to continue...")
spark.stop()