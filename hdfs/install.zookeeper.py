


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
# Create the /var/lib/zookeeper/data/myid file and edit it to contain the host’s ID:

# echo 1 > /var/lib/zookeeper/data/myid










  
  
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

  
  
