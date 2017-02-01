
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













