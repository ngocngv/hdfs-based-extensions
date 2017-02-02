


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

  
  
  
  
  
  
