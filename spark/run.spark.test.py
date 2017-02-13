


# https://dwbi.org/etl/bigdata/201-install-spark-in-hadoop-cluster






# create a HDFS directory to park the output file.
hadoop fs -mkdir -p /spark_analytics


hadoop fs -ls /


# Login to Spark shell.
$SPARK_HOME/bin/spark-shell --master spark://yarn1.local:7077






scala> val rdd_profit = sc.textFile("/pig_analytics/Profit_Q1.txt")
rdd_profit: org.apache.spark.rdd.RDD[String] = /pig_analytics/Profit_Q1.txt MapPartitionsRDD[1] at textFile at :24

scala> rdd_profit.partitions.length
res0: Int = 2

scala> rdd_profit.count()
res1: Long = 17

scala> val header = rdd_profit.first()
header: String = Country|Date|Profit|Currency

scala> rdd_profit.take(3)
res2: Array[String] = Array(Country|Date|Profit|Currency, INDIA|2016-01-31|4500000|INR, US|2016-01-31|9000000|USD)

scala> val rdd_profit_nohdr = rdd_profit.filter(row => row != header)
rdd_profit_nohdr: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[2] at filter at :28

scala> rdd_profit_nohdr.take(3)
res3: Array[String] = Array(INDIA|2016-01-31|4500000|INR, US|2016-01-31|9000000|USD, SINGAPORE|2016-01-31|7000000|SGD)

scala> val rdd_profit_split = rdd_profit_nohdr.map(line => line.split("\\|"))
rdd_profit_split: org.apache.spark.rdd.RDD[Array[String]] = MapPartitionsRDD[3] at map at :30

scala> val rdd_profit_KV = rdd_profit_split.map{ (x) => (x(0), if( x(2).isEmpty) 0 else x(2).toInt ) }
rdd_profit_KV: org.apache.spark.rdd.RDD[(String, Int)] = MapPartitionsRDD[4] at map at :32

scala> val rdd_profit_xAus = rdd_profit_KV.filter{case (key, value) => key != "AUSTRALIA"}
rdd_profit_xAus: org.apache.spark.rdd.RDD[(String, Int)] = MapPartitionsRDD[5] at filter at :34

scala> val rdd_profit_q1 = rdd_profit_xAus.reduceByKey((v1,v2) => v1 + v2)
rdd_profit_q1: org.apache.spark.rdd.RDD[(String, Int)] = ShuffledRDD[6] at reduceByKey at :34

scala> rdd_profit_q1.collect()
res4: Array[(String, Int)] = Array((US,35900000), (SINGAPORE,28600000), (INDIA,19200000))

scala> rdd_profit_q1.repartition(1).saveAsTextFile("/spark_analytics/profit")

scala> :quit
















