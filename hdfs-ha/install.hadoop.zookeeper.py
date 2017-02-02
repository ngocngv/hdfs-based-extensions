
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

