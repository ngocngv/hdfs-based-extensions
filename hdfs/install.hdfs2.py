



## Add FQDN Mapping: /etc/hosts
#------------------------------------------------------------------------------
10.10.0.1      nn1.hdfs   dn1.hdfs
10.10.0.2      nn2.hdfs   dn2.hdfs   coord1 gtm1  rm1.rad
10.10.0.3      nn3.hdfs   dn3.hdfs   coord2 gtm2  rm2.rad
10.10.0.4      dn4.hdfs
10.10.0.5      dn5.hdfs




## Install Java JRE
yum install java-1.8.0-openjdk

## Install Java JDK
yum install java-1.8.0-openjdk-devel

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



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


