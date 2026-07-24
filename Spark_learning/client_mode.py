from pyspark.sql import SparkSession
import os 

spark=SparkSession.builder\
    .appName("NilamDemo")\
    .getOrCreate()

sc=spark.sparkContext
print("="*50)
print("DRIVER PROCESS")
print("Driver ID",os.getpid())
print("="*50)

data=[1,2,3,4,5,6,7,8]

rdd=sc.parallelize(data,4)
def process_partition(partition):
    import os
    print(f"Executor ID={os.getpid()}")
    result=[]
    for num in partition:
        result.append(num*num)
    return result 

output=rdd.mapPartitions(process_partition).collect()

print("\n FInal Result Recevied by Driver:")
print(output)
input("Please Presss Enter to end the process")
spark.stop()

spark-submit --master spark://127.0.0.1:7077 --deploy-mode client client_mode.py