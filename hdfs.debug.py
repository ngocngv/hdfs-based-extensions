


# the status and health of a cluster?
bin/hadoop dfsadmin -report

hadoop dfsadmin -report | grep ^Name


# https://discuss.pivotal.io/hc/en-us/sections/115000443768-YARN



# How to Collect YARN job logs
# https://discuss.pivotal.io/hc/en-us/articles/228988107-How-to-Collect-YARN-job-logs
yarn application -list -appStates FINISHED,FAILED,KILLED

yarn application -list -appStates ALL 



# Reviewing the YARN ResourceManager UI available via Ambari GUI / YARN / Quick Links / ResourceManager UI: 
http://yarn1.local:23188/cluster
http://yarn2.local:23188/cluster
    
    
# Run the following command to fetch and compress the logs:
yarn logs -applicationId <app_id> -appOwner <user> |& gzip -c > <app_id>.log.gz

# The option -appOwner can be omitted if the current user is the same user who ran the job.


    
    
    
    
    
    
# How To Recover YARN Resource Manager State from Standby to Active
# https://discuss.pivotal.io/hc/en-us/articles/231707287-How-To-Recover-YARN-Resource-Manager-State-from-Standby-to-Active

# Resource Manager logs show the following error:
# org.apache.hadoop.ha.ServiceFailedException: RM could not transition to Active ERROR resourcemanager.ResourceManager (ResourceManager.java:serviceStart(599)) - Failed to load/recover state 
  

# Resolution
# Clear the Resource Manager state in zookeeper with the below steps:
yarn resourcemanager -format-state-store
















