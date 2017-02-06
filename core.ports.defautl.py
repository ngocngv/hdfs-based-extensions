
# https://github.com/angelcervera/docker-hadoop/blob/master/Dockerfile


################### Expose ports
### Core


# Zookeeper
2181

# NameNode metadata service ( fs.defaultFS )
9000

# FTP Filesystem impl. (fs.ftp.host.port)
21



### Hdfs ports (Reference: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
#-----------------------------------------------------------------------------------------------------------------

# NameNode Web UI: Web UI to look at current status of HDFS, explore file system (dfs.namenode.http-address / dfs.namenode.https-address)
50070
50470

# DataNode : DataNode WebUI to access the status, logs etc. (dfs.datanode.http.address / dfs.datanode.https.address)
50075
50475

# DataNode  (dfs.datanode.address / dfs.datanode.ipc.address)
50010
50020

# Secondary NameNode (dfs.namenode.secondary.http-address / dfs.namenode.secondary.https-address)
50090
50090

# Backup node (dfs.namenode.backup.address / dfs.namenode.backup.http-address)
50100
50105

# Journal node (dfs.journalnode.rpc-address / dfs.journalnode.http-address / dfs.journalnode.https-address )
8485
8480
8481













