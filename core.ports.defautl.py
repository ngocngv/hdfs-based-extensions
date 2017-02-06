
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
50070 50470

# DataNode : DataNode WebUI to access the status, logs etc. (dfs.datanode.http.address / dfs.datanode.https.address)
50075 50475

# DataNode  (dfs.datanode.address / dfs.datanode.ipc.address)
50010 50020

# Secondary NameNode (dfs.namenode.secondary.http-address / dfs.namenode.secondary.https-address)
50090 50090

# Backup node (dfs.namenode.backup.address / dfs.namenode.backup.http-address)
50100 50105

# Journal node (dfs.journalnode.rpc-address / dfs.journalnode.http-address / dfs.journalnode.https-address )
8485 8480 8481



### Mapred ports (Reference: https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
#-----------------------------------------------------------------------------------------------------------------

# Task Tracker Web UI and Shuffle (mapreduce.tasktracker.http.address)
50060

# Job tracker Web UI (mapreduce.jobtracker.http.address)
50030

# Job History Web UI (mapreduce.jobhistory.webapp.address)
19888

# Job History Admin Interface (mapreduce.jobhistory.admin.address)
10033

# Job History IPC (mapreduce.jobhistory.address)
10020



### Yarn ports (Reference: https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
#-----------------------------------------------------------------------------------------------------------------

# Applications manager interface (yarn.resourcemanager.address)
8032

# Scheduler interface (yarn.resourcemanager.scheduler.address)
8030

# Resource Manager Web UI (yarn.resourcemanager.webapp.address / yarn.resourcemanager.webapp.https.address)
8088 8090

# ??? (yarn.resourcemanager.resource-tracker.address)
8031

# Resource Manager Administration Web UI
8033

# Address where the localizer IPC is (yarn.nodemanager.localizer.address)
8040

# Node Manager Web UI (yarn.nodemanager.webapp.address)
8042

# Timeline servise RPC (yarn.timeline-service.address)
10200

# Timeline servise Web UI (yarn.timeline-service.webapp.address / yarn.timeline-service.webapp.https.address)
8188 8190

# Shared Cache Manager Admin Web UI (yarn.sharedcache.admin.address)
8047

# Shared Cache Web UI (yarn.sharedcache.webapp.address)
8788

# Shared Cache node manager interface (yarn.sharedcache.uploader.server.address)
8046

# Shared Cache client interface (yarn.sharedcache.client-server.address)
8045



### Other ports
#-----------------------------------------------------------------------------------------------------------------

# SSH
22







