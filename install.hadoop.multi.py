
# https://github.com/kiwenlau/hadoop-cluster-docker
# http://user501254.github.io/BD_STTP_2016/hadoop-multi-node-cluster-installation-guide/
# http://fibrevillage.com/storage/617-hadoop-2-7-cluster-installation-and-configuration-on-rhel7-centos7  
# http://www.tecmint.com/install-configure-apache-hadoop-centos-7/


# Hadoop Common: – it contains the Java libraries and utilities needed by other Hadoop modules.
# HDFS: – Hadoop Distributed File System – A Java based scalable file system distributed across multiple nodes.
# MapReduce: – YARN framework for parallel big data processing.
# Hadoop YARN: A framework for cluster resource management.



# Setup cluster information:
hostnamectl set-hostname master
hostnamectl set-hostname slave1
hostnamectl set-hostname slave2




# Install Java
java -version 


# Create User Account
useradd -d /opt/hadoop hadoop
passwd hadoop


# Add FQDN Mapping: /etc/hosts
10.10.0.1 hadoop-namenode
10.10.0.11 hadoop-datanode-01
10.10.0.12 hadoop-datanode-02


# Configuring SSH key pair login
su - hadoop
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@hadoop-namenode
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@hadoop-datanode-01
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@hadoop-datanode-02
chmod 0600 ~/.ssh/authorized_keys
exit


# Download and Extract Hadoop Source
# su - hadoop
cd /opt
wget http://www-us.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
tar xzf hadoop-2.7.3.tar.gz
mv hadoop-2.7.3 hadoop

chown -R hadoop:hadoop /opt/hadoop/
  

# Setup Environment Variables
# su - hadoop
# ~/.bashrc  
# ~/.bash_profile


## JAVA env variables
export JAVA_HOME=/usr/java/default
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar
## HADOOP env variables
export HADOOP_HOME=/opt/hadoop
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
    
#    
export HADOOP_INSTALL=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME



# apply the changes in current running environment
source ~/.bashrc

source ~/.bash_profile
echo $HADOOP_HOME
echo $JAVA_HOME


















