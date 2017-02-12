

# https://dwbi.org/etl/bigdata/201-install-spark-in-hadoop-cluster



# Master Server Setup
#------------------------------------------------------------------------------  
cd /opt

wget http://www-us.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz
  
tar xzf spark-2.1.0-bin-hadoop2.7.tgz
mv spark-2.1.0-bin-hadoop2.7.tgz spark

chown -R spark:spark /opt/spark/




#
# Setup Environment Variables   
#------------------------------------------------------------------------------  
su - spark  
# edit ~/.bashrc  |  ~/.bash_profile
  

## Spark env variables
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin



# apply the changes in current running environment
source ~/.bashrc

echo $SPARK_HOME 





# To configure Spark environment script in order to set the Java Home & Hadoop configuration directory
cd $SPARK_HOME/conf

cp spark-env.sh.template spark-env.sh


# edit spark-env.sh
#-------------------------------------------------------------
export JAVA_HOME=/usr/java/default

export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

export SPARK_WORKER_CORES=6



# edit slaves
#-------------------------------------------------------------
DataNode1
DataNode2







# Slave Server Setup
#------------------------------------------------------------------------------  


# copy the spark directory with the binaries and configuration files from the NameNode to the DataNodes.
scp -r /opt/spark spark@datanode1:/opt/spark
scp -r /opt/spark spark@datanode2:/opt/spark


  
# Setup Environment Variables   
# edit ~/.bashrc  |  ~/.bash_profile

## Spark env variables
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin


# apply the changes in current running environment
source ~/.bashrc

echo $SPARK_HOME 






















