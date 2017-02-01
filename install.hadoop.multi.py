
# https://github.com/kiwenlau/hadoop-cluster-docker
# http://user501254.github.io/BD_STTP_2016/hadoop-multi-node-cluster-installation-guide/
# http://fibrevillage.com/storage/617-hadoop-2-7-cluster-installation-and-configuration-on-rhel7-centos7  
# http://www.tecmint.com/install-configure-apache-hadoop-centos-7/


# Hadoop Common: – it contains the Java libraries and utilities needed by other Hadoop modules.
# HDFS: – Hadoop Distributed File System – A Java based scalable file system distributed across multiple nodes.
# MapReduce: – YARN framework for parallel big data processing.
# Hadoop YARN: A framework for cluster resource management.

# http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html



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
# download hadoop latest available version from its official site at hadoop-namenode server only.
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



# Edit $HADOOP_HOME/etc/hadoop/hadoop-env.sh file and set JAVA_HOME environment variable. 
# Change the JAVA path as per install on your system.
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-oracle.x86_64/
export HADOOP_OPTS=-Djava.net.preferIPv4Stack=true

# export JAVA_HOME=/usr/java/default/



#-----------------------------------------------------------------------
# Configure Hadoop
#-----------------------------------------------------------------------

cd $HADOOP_HOME/etc/hadoop


# Edit core-site.xml
#-----------------------------------------------------------------------
#Add the following inside the configuration tag
<property>
    <name>fs.default.name</name>
    <value>hdfs://hadoop-namenode:9000/</value>
</property>
<property>
    <name>dfs.permissions</name>
    <value>false</value>
</property>



# Edit hdfs-site.xml
#-----------------------------------------------------------------------
# Add the following inside the configuration tag
<property>
	  <name>dfs.data.dir</name>
	  <value>/opt/hadoop/dfs/name/data</value>
	  <final>true</final>
</property>
<property>
	  <name>dfs.name.dir</name>
	  <value>/opt/hadoop/dfs/name</value>
	  <final>true</final>
</property>
<property>
	  <name>dfs.replication</name>
	  <value>1</value>
</property>



# Use /opt/volume/ directory to store our hadoop file system.
# Replace the dfs.data.dir and dfs.name.dir values accordingly.
<property>
    <name>dfs.data.dir</name>
    <value>file:///opt/volume/datanode</value>
</property>
<property>
    <name>dfs.name.dir</name>
    <value>file:///opt/volume/namenode</value>
</property>


# su root
mkdir -p /opt/volume/namenode
mkdir -p /opt/volume/datanode
chown -R hadoop:hadoop /opt/volume/
# ls -al /opt/  #Verify permissions
# exit          #Exit root account to turn back to hadoop user




# Edit mapred-site.xml
#-----------------------------------------------------------------------
# Add the following inside the configuration tag
<property>
    <name>mapred.job.tracker</name>
	  <value>hadoop-namenode:9001</value>
</property>



<property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
</property>



# Edit yarn-site.xml
#-----------------------------------------------------------------------
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>






#-----------------------------------------------------------------------
# Copy Hadoop folder to Slave Servers
#-----------------------------------------------------------------------
# su - hadoop
rsync -auvx $HADOOP_HOME hadoop-datanode-1:$HADOOP_HOME
rsync -auvx $HADOOP_HOME hadoop-datanode-2:$HADOOP_HOME


  
# Configure Hadoop on namenode Server Only
# su - hadoop
cd $HADOOP_HOME/etc/hadoop
vim slaves
hadoop-datanode-1
hadoop-datanode-2


# Format Hadoop Namenode
# Format Name Node on Hadoop Master only
# su - hadoop
hadoop namenode -format
hdfs namenode -format



#-----------------------------------------------------------------------
# Configure Hadoop on datanode server Only
#-----------------------------------------------------------------------

# Edit hdfs-site.xml
#-----------------------------------------------------------------------
# Add the following inside the configuration tag
<property>
	  <name>dfs.data.dir</name>
	  <value>/opt/hadoop/dfs/name/data</value>
	  <final>true</final>
</property>


# Start Hadoop Services
# Use the following command to start all hadoop services on hadoop namenode and datanodes
start-dfs.sh

# start-yarn.sh




# Test Hadoop cluster(Multiple Nodes) Setup
#-----------------------------------------------------------------------

# On namenode, make the HDFS directories required using following commands.
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hadoop

# Now copy all files from local file system /home/hadoop/etc/hadoop/hadoop-env.sh to hadoop distributed file system using below command
hdfs dfs -put /home/hadoop/hadoop-2.7.3.tar /user/hadoop


# Now browse hadoop distributed file system by opening below url in browser.
http://<hadoopnode>:50070/explorer.html#/user/hadoop/

# Now copy logs directory for hadoop distributed file system to local file system.
hdfs dfs -get /user/hadoop/hadoop-2.7.3.tar /home/test
    
    
    
    
# Check Hadoop cluster status
hdfs dfsadmin -report      
    
    
    
    
    
    
    
