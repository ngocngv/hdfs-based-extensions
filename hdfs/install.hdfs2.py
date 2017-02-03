



## Add FQDN Mapping: /etc/hosts
#------------------------------------------------------------------------------
10.10.0.1      nn1.hdfs   dn1.hdfs    zk01
10.10.0.2      nn2.hdfs   dn2.hdfs    zk02      coord1 gtm1  rm1.rad
10.10.0.3      nn3.hdfs   dn3.hdfs    zk03      coord2 gtm2  rm2.rad
10.10.0.4      dn4.hdfs
10.10.0.5      dn5.hdfs




## Install Java JRE
yum install java-1.8.0-openjdk
yum install java-1.8.0-openjdk.x86_64
yum install java-1.8.0-openjdk-headless.x86_64

## Install Java JDK
yum install java-1.8.0-openjdk-devel.x86_64

#
java -version 



# Create User Account
#------------------------------------------------------------------------------
useradd -d /opt/hadoop -m hadoop
passwd hadoop

#
echo "hadoop ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/hadoop
chmod 0440 /etc/sudoers.d/hadoop





# Configuring SSH key pair login
#------------------------------------------------------------------------------
su - hadoop

ssh-keygen -t rsa

ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@nn1.hdfs
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@nn2.hdfs
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@nn3.hdfs

ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@dn4.hdfs
ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@dn5.hdfs

chmod 0600 ~/.ssh/authorized_keys
exit


#
for i in nn1.hdfs nn2.hdfs nn3.hdfs; do 
ssh-copy-id $i;
done





# Download and Extract Hadoop Source
#------------------------------------------------------------------------------
su - hadoop

cd /opt
wget http://www-us.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
tar xzf hadoop-2.7.3.tar.gz
mv hadoop-2.7.3 hadoop

chown -R hadoop:hadoop /opt/hadoop/



  
  
#
# Setup Environment Variables   
#------------------------------------------------------------------------------  
su - hadoop  
# edit ~/.bashrc  |  ~/.bash_profile
  
# Create Java Symlink
#mkdir -p /usr/java/default/bin/
#ln -s /usr/lib/jvm/jre-1.8.0-openjdk/bin/java /usr/java/default/bin/java


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
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
#
export YARN_HOME=$HADOOP_HOME
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
#
export ZOOKEEPER_HOME=/opt/zookeeper
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$ZOOKEEPER_HOME/bin 
  
  
  
  
# apply the changes in current running environment
source ~/.bashrc

echo $JAVA_HOME 
echo $HADOOP_HOME 
echo $ZOOKEEPER_HOME
  
  
  

  
  
# Copy the Java and Hadoop-2.x, zookeeper-3.x directories, and .bashrc file to all the nodes (Standby namenode, datanode)
scp –r <path of directory> hadoop@<ipaddr>:<path where you need to copy>



  
#  created datanode directory to store the blocks.
mkdir -p /opt/hadoop/datanode/data1
mkdir -p /opt/hadoop/datanode/data2
mkdir -p /opt/hadoop/datanode/data3


#
mkdir -p /opt/hadoop/namenode


# Change the permission to datanode directory.
chmod 0755 /opt/hadoop/datanode/data1

chown -R hadoop:hadoop /opt/hadoop/
  
  
  
  
  
  
  
  

