

# http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html



# https://www.edureka.co/blog/interview-questions/hadoop-interview-questions-hadoop-cluster/?utm_source=blog&utm_medium=left-menu&utm_term=Hadoop%20Interview%20Questions%20%E2%80%93%20Setting%20Up%20Hadoop%20Cluster


/sbin/start-yarn.sh

./sbin/yarn-daemon.sh start resourcemanager
./sbin/yarn-daemon.sh start nodemanager



./sbin/hadoop-daemon.sh start namenode
./sbin/hadoop-daemon.sh start datanode
./sbin/yarn-daemon.sh start resourcemanager
./sbin/yarn-daemon.sh start nodemanager
./sbin/mr-jobhistory-daemon.sh start historyserver
