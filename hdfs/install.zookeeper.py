


# Create User Account
#------------------------------------------------------------------------------
useradd -d /opt/zookeeper -m zookeeper
passwd zookeeper

#
echo "zookeeper ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/zookeeper
chmod 0440 /etc/sudoers.d/zookeeper




# Download and Extract Zookeeper Source
#------------------------------------------------------------------------------
su - zookeeper

cd /opt
wget https://archive.apache.org/dist/zookeeper/zookeeper-3.4.9/zookeeper-3.4.9.tar.gz
tar xzf zookeeper-3.4.9.tar.gz
mv zookeeper-3.4.9 zookeeper

chown -R zookeeper:zookeeper /opt/zookeeper/

  
  
  
# https://docs.midonet.org/docs/latest/quick-start-guide/rhel-7_kilo-rdo/content/_zookeeper_installation.html


  
#  
# /opt/zookeeper/conf/zoo_sample.cfg 
cp zoo_sample.cfg zoo.cfg  


# Create data directory:
mkdir -p /opt/zookeeper/data
chown -R zookeeper:zookeeper /opt/zookeeper/data


# Node-specific Configuration:

#ZK Node 01
# Create the /opt/zookeeper/data/myid file and edit it to contain the host’s ID:
echo '1' > /opt/zookeeper/data/myid

#ZK Node 02
echo '2' > /opt/zookeeper/data/myid

#ZK Node 03
echo '3' > /opt/zookeeper/data/myid


# 
chown -R zookeeper:zookeeper /opt/zookeeper/data/myid

  
  

# Edit /etc/systemd/system/zookeeper.service

## Loaded
systemctl daemon-reload
systemctl enable zookeeper
systemctl start zookeeper



# Verify ZooKeeper Operation
#------------------------------------------------------------------------------

# A basic check can be done by executing the ruok (Are you ok?) command on all nodes. 
# This will reply with imok (I am ok.) if the server is running in a non-error state:

echo ruok | nc 127.0.0.1 2181
# imok


# More detailed information can be requested with the stat
echo stat | nc 127.0.0.1 2181












  
  
# https://docs.midonet.org/docs/latest/quick-start-guide/rhel-7_kilo-rdo/content/_zookeeper_installation.html   
  
# start zookeeper
bin/zkServer.sh start

# if you need to stop
bin/zkServer.sh stop

# check if the process is running
ps -aux | grep java

# check for QuorumPeerMain

# check the status of each server to see if they are in a cluster. 
# Only one among the 3 should be master and the others are followers
bin/zkServer.sh status

  
  
