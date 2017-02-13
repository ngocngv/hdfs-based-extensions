


# Launching Applications with spark-submit
# http://spark.apache.org/docs/latest/submitting-applications.html




./bin/spark-submit \
    --class <main-class> \
    --master <master-url> \
    --deploy-mode <deploy-mode> \
    --conf <key>=<value> \
    ... # other options
    
    <application-jar> \
    [application-arguments]



    
    
    
    
    
# run the Spark example job
./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master spark://yarn1.local:7077 \
    ./examples/jars/spark-examples_2.11-2.1.0.jar \
    1000
    
    


# Run on a Spark standalone cluster in client deploy mode
./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master spark://yarn1.local:7077 \
    --executor-memory 2G \
    --total-executor-cores 4 \
    ./examples/jars/spark-examples_2.11-2.1.0.jar \
    1000

  
  
  
# Run on a Spark standalone cluster in cluster deploy mode with supervise
./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master spark://yarn1.local:7077 \
    --deploy-mode cluster \
    --supervise \
    --executor-memory 2G \
    --total-executor-cores 4 \
    ./examples/jars/spark-examples_2.11-2.1.0.jar \
    1000
  
  
  
  
  
  
  
# Run on a YARN cluster
#-------------------------------------------------------------------------------------

export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \  # can be client for client mode
    --executor-memory 2G \
    --num-executors 50 \
    ./examples/jars/spark-examples_2.11-2.1.0.jar \
    1000
  
  
  
  
  
  
# Run a Python application on a Spark standalone cluster
#-------------------------------------------------------------------------------------

./bin/spark-submit \
    --master spark://yarn1.local:7077 \
    ./examples/src/main/python/pi.py \
    1000
  
  
  
# Run on a Mesos cluster in cluster deploy mode with supervise
./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master spark://yarn1.local:7077 \
    --deploy-mode cluster \
    --supervise \
    --executor-memory 2G \
    --total-executor-cores 4 \
    http://path/to/examples.jar \
    1000
  
  
  
  
  
  
  
  
  
  
  
