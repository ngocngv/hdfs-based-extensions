
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
50070       dfs.namenode.http-address
50470       dfs.namenode.https-address

# DataNode : DataNode WebUI to access the status, logs etc. (dfs.datanode.http.address / dfs.datanode.https.address)
50075       dfs.datanode.http.address
50475       dfs.datanode.https.address

# DataNode  (dfs.datanode.address / dfs.datanode.ipc.address)
50010       dfs.datanode.address
50020       dfs.datanode.ipc.address

# Secondary NameNode (dfs.namenode.secondary.http-address / dfs.namenode.secondary.https-address)
50090       dfs.namenode.secondary.http-address
50090       dfs.namenode.secondary.https-address

# Backup node (dfs.namenode.backup.address / dfs.namenode.backup.http-address)
50100       dfs.namenode.backup.address
50105       dfs.namenode.backup.http-address

# Journal node (dfs.journalnode.rpc-address / dfs.journalnode.http-address / dfs.journalnode.https-address )
8485        dfs.journalnode.rpc-address
8480        dfs.journalnode.http-address
8481        dfs.journalnode.https-address













