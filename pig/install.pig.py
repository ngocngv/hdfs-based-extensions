

# https://dwbi.org/etl/bigdata/198-install-pig-in-client-node-of-hadoop-cluster





# Install PIG

cd /opt/

wget http://www-us.apache.org/dist/pig/pig-0.16.0/pig-0.16.0.tar.gz

tar xzf pig-0.16.0.tar.gz
mv pig-0.16.0 pig




#
# set the PIG Environment variables
#------------------------------------------------------------------------------  

# edit ~/.bashrc  |  ~/.bash_profile


## Pig env variables
export PIG_HOME=/opt/pig
export PATH=$PATH:$PIG_HOME/bin

export CLASSPATH=$CLASSPATH:/opt/pig/lib/*:.
export PIG_CLASSPATH=$HADOOP_HOME/etc/hadoop





# apply the changes in current running environment
source ~/.bashrc

echo $PIG_HOME 









