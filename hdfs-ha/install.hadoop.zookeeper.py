
# https://www.edureka.co/blog/how-to-set-up-hadoop-cluster-with-hdfs-high-availability/



172.31.8.4      host01 dn1.rad 
172.31.8.5      host02 nn1.rad dn2.rad coord1 gtm1 rm1.rad
172.31.8.6      host03 nn2.rad dn3.rad coord2 gtm2 rm2.rad



10.10.0.1      dn1.hdfs

10.10.0.2      nn1.hdfs   dn2.hdfs   coord1 gtm1 rm1.rad
10.10.0.3      nn2.hdfs   dn3.hdfs   coord2 gtm2 rm2.rad



