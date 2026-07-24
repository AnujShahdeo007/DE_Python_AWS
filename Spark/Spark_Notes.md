Main Components of Spark Architecture:

1. Driver Program 

 - Driver is the brain of spark 
 - Your python/pyspark scriptys runs inside the Driver 

 <!-- from pyspark.sql import sparkSession 
spark=SparkSession.builder.appname("abc").getOrCreate()
df=spark.read.csv("sales.csv")
df.groupBy("city").sum("amount").show() -->

Responsibilities:

Driver:
- Read your code 
- create execution plan 
- Request resources 
- Divide work 
- Sends task to worker node 
- Collects result 

2. SparkSession/Spark Context 

- SparkSession 
- Entry point to Spark application 
- It is the first object developers use to interct with spark 

# Why SparkSession was Introduced?
- Before Spark 2.0 
- too many objects 

Spark 2.0 introduces :
- SparkSession
- One object for everything 

# What SparkSession Provides?
- Dataframes 
- SQl
- Hive 
- Catalog 
- Configurations 

# Internal Structure of SparkSession 

SparkSession 
    |
    +--Spark Context 
    |
    +-- SQL Enginer 
    |
    +-- Dataframe Engine
    |
    +-- Catalog 
    |
    +-- Configurations 

# What happens When Spark Session is Created 

spark= SparkSession.builder.appName("Emp").master("local[*]").getOrCreate()

Step 1:

Python Starts - Python Process 

Step 2 :

Pyspark libraries load  - Pyspark Loaded 

Step 3 : 

Builder stores configurations - Application name, master, Memory setting 

Step 4 :

getOrCreate() execute - Existing Session Avilable? If yes - Return Existing Session . If No - Create New Session 

Step 5 : 

JVM starts 

    Python 
      |
    Py4J 
      |
    JVM 

Note: Spark Engine runs inside JVM 

Step 6 :

Spark Context is created - Spark Context is created and returned to SparkSession

SparkSession 
    |
SparkContext

Step 7: 

Driver Process Starts 

Driver Program 

Step 8:

Cluster connection established 

- Local 
- YARN 
- Standalone 
- Kubernetes 

Step 9 :

SparkSession return 

spark 


---------- Now Application is ready --------------------

3. Cluster Manager 
- Responsibale for resource allocation 
- Standalone 
- YARN 
- Kubernetes 
- Mesos 

- Driver asks for resources and the cluster manager decides where to allocate him. 

from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("Spark Learning").master("local[*]").getOrCreate()

4. Worker Nodes 


5. Executors 
6. Tasks 
7. Jobs 
8. Stages 
9. DAg scheduler 
10. Task scheduler 
11. Cache memory 
12. Cluster mode vs Client mode  & Local mode 

<!-- from pyspark.sql import sparkSession 
spark=SparkSession.builder.appname("abc").getOrCreate()
df=spark.read.csv("sales.csv")
df.groupBy("city").sum("amount").show() -->

============================================================================================

What is RDD: A distributed collection of data that can be processed in parallel 
             across multiple machines. 

R - Resilient - spark is resilient because it maintains lineage information for every RDD. 
                If a node or partition fails, Spark can automatically recompute only lost partition using linege grapgh insted of reprocessing the entire dataset. 

              - Able to recover from failure 
              - This is why RDDs are Fault Torelent 

          What Is Fault Tolernce ?
          - Fault tolrance is Spark's ability to recover lost data automatically if any failure 
            occures during excution.

          - Spark can rebuild lost data instead of storing multiple copies 


          How Spark Achives Fault Torlance :

          1. RDD Immutablity 

          2. Lineage Graph : Spark Remembers - How Every RDD was Created 


D - Distributed : The data is distributed across multiple executors 


D - Dataset - An RDD is simply  dataset ( Collection of records)


Important Properties of an RDD:

1. Immutable 

  - Once created, an RDD cannot be changed

  - rdd=sc.parallelize([1,2,3,4]) # rdd- 1,2,3,4
  - rdd2=rdd.map(lambda x:x*2) # rdd2 - 2,4,6,8

  Spark creates a new RDD instead of modifying the old one 

  Why immutable:

  - Easier parllel processing 
  - No synchronization issues 
  - Better fault tolarace 
  - Simpler recovert using linage 

2. Distributed 

  - An RDD is divided into partitions 

  - Each partition can be processed independently 

3. Fault Tolrance 

- Spark Maintains the lineage of every RDD 

- Fault tolrance is Spark's ability to recover lost data automatically if any failure 
   occures during excution.


4. Lazy Evaluation 

- 

- Because Spark waits until it is absolutly necessary 



