


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
    --master mesos://yarn1.local:7077 \
    --deploy-mode cluster \
    --supervise \
    --executor-memory 2G \
    --total-executor-cores 4 \
    http://path/to/examples.jar \
    1000

    
    
    
    
    
    
    
# Master URLs
#-------------------------------------------------------------------------------------

spark://HOST:PORT           # Connect to the given Spark standalone cluster master. 
                            # The port must be whichever one your master is configured to use, which is 7077 by default.

mesos://HOST:PORT           # Connect to the given Mesos cluster. 
                            # The port must be whichever one your is configured to use, which is 5050 by default. 
                            # Or, for a Mesos cluster using ZooKeeper, use mesos://zk://.... To submit with --deploy-mode cluster, the HOST:PORT should be configured to connect to the MesosClusterDispatcher.
                
yarn                        # Connect to a YARN cluster in client or cluster mode depending on the value of --deploy-mode. 
                            # The cluster location will be found based on the HADOOP_CONF_DIR or YARN_CONF_DIR variable.

    
    
    
    
    
    
    
    
    
    
