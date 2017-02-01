

# http://fibrevillage.com/storage/628-how-to-add-a-new-datanode-to-a-running-hadoop-cluster


# Install Java
java -version


# Create User Account
useradd -d /opt/hadoop hadoop
passwd hadoop


# Add FQDN Mapping: /etc/hosts
10.10.0.1 hadoop-namenode
10.10.0.11 hadoop-datanode-01
10.10.0.12 hadoop-datanode-02
10.10.0.13 hadoop-datanode-03



# Configuring SSH key pair login
# su - hadoop
# ssh-keygen -t rsa

ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@hadoop-datanode-03
chmod 0600 ~/.ssh/authorized_keys
exit



# Copy Hadoop folder to Slave Servers
#-----------------------------------------------------------------------
# su - hadoop
rsync -auvx /home/hadoop/.bashrc hadoop-datanode-03:/home/hadoop/
rsync -auvx $HADOOP_HOME hadoop-datanode-03:$HADOOP_HOME


  
# Configure Hadoop on namenode Server Only
#-----------------------------------------------------------------------
# su - hadoop
cd $HADOOP_HOME/etc/hadoop
vim slaves
hadoop-datanode-01
hadoop-datanode-02
hadoop-datanode-03



# Configure Hadoop on new datanode server Only
#-----------------------------------------------------------------------

# Edit hdfs-site.xml
#-----------------------------------------------------------------------
# Add the following inside the configuration tag
<property>
    <name>dfs.data.dir</name>
    <value>/opt/hadoop/dfs/name/data</value>
    <final>true</final>
</property>




# Start datanode Hadoop Services
#-----------------------------------------------------------------------

# On namenode, run
start-dfs.sh

# Or, on new datanode, run
hadoop-daemon.sh start datanode



# Check Hadoop cluster status
#-----------------------------------------------------------------------

# On any of hadoop cluster node, run
hdfs dfsadmin -report 




