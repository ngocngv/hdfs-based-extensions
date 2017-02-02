
# https://www.edureka.co/blog/how-to-set-up-hadoop-cluster-with-hdfs-high-availability/



172.31.8.4      host01 dn1.rad 
172.31.8.5      host02 nn1.rad dn2.rad coord1 gtm1 rm1.rad
172.31.8.6      host03 nn2.rad dn3.rad coord2 gtm2 rm2.rad



10.10.0.1      dn1.hdfs

10.10.0.2      nn1.hdfs   dn2.hdfs   coord1 gtm1 rm1.rad
10.10.0.3      nn2.hdfs   dn3.hdfs   coord2 gtm2 rm2.rad




# Change the directory to zookeeper’s conf directory.
cp zoo_sample.cfg zoo.cfg

# add
server.1=dn1.hdfs:2888:3888
server.2=nn1.hdfs:2888:3888
server.3=nn2.hdfs:2888:3888

    
    
# Copy the Java and Hadoop-2.x, zookeeper-3.x directories, and .bashrc file to all the nodes (Standby name node, Data node) using scp command.
scp –r <path of directory> hadoop@<ipaddr>:<path where you need to copy>


    
    
#  created datanode directory to store the blocks.
mkdir -p /opt/hadoop/datanode/data1
mkdir -p /opt/hadoop/datanode/data2
mkdir -p /opt/hadoop/datanode/data3

chmod /opt/hadoop/datanode/data1
chmod /opt/hadoop/datanode/data2
chmod /opt/hadoop/datanode/data3




# Create the myid file
# dataDir=/opt/zookeeper/data
echo '3' > /opt/zookeeper/data/myid




# Start the Journalnode in all the three nodes.
hadoop-daemon.sh start journalnode
jps


# Format the Active namenode.
hdfs namenode -format


# Start the Namenode daemon in Active namenode.
hadoop-daemon.sh start namenode
jps



# Copy the HDFS Metadata from Active Namenode to Standby Namenode.
hdfs namenode -bootstrapStandby



# Start the namenode daemon in Standby namenode machine.
#-----------------------------------------------------------------------
hadoop-daemon.sh start namenode



# Now start the Zookeeper service in all the three nodes.
#-----------------------------------------------------------------------
# Start zookeeper in Active NameNode.
# Start zookeeper in Standby NameNode.
# Start zookeeper in DataNode.

zkServer.sh start

# After running the Zookeeper server, enter JPS command. 
# In all the nodes you will see the "QuorumPeerMain" service.
jps



# Start the Datanode daemon in Datanode machine.
#-----------------------------------------------------------------------
hadoop-daemon.sh start datanode



# Start the Zookeeper fail over controller in Active namenode and standby namenode.
#-----------------------------------------------------------------------

# Format the zookeeper fail over controller in Active namenode.
hdfs zkfc –formatZK

# Start the ZKFC in Active namenode.
hadoop-daemon.sh start zkfc

# Enter jps command to check the DFSZkFailoverController daemons.


# Format the zookeeper fail over controller in Standby namenode.
hdfs zkfc –formatZK

# Start the ZKFC in Standby namenode.
hadoop-daemon.sh start zkfc

# Enter jps command to check the DFSZkFailoverController daemons.





# Now check the status of each Namenode, which node is Active or which node is on Standby
hdfs haadmin –getServiceState nn1
hdfs haadmin –getServiceState nn2






















