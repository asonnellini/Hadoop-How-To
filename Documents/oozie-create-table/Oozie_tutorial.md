# How to create an External table and a ORC table on Hive using OOZIE

## Overview

The target of this tutorial is to use oozie to automate the creation of the External
and ORC tables in Hive [that was detailed in the previous tutorial](https://github.com/asonnellini/Hadoop-How-To/blob/master/Documents/Create-Hive-Table/Hadoop-How-to-Hive-Create-Table.md#overview).

We expect oozie to be already configured server side.

Sample files mentioned in the below tutorials are uploaded on this github folder.

## Steps

  - Connect to the Edge Node

  - Create 3 hql scripts – you can refer to the [previous tutorial](https://github.com/asonnellini/Hadoop-How-To/blob/master/Documents/Create-Hive-Table/Hadoop-How-to-Hive-Create-Table.md#overview) for
    further details:
    
      - CREATE\_EXTERNAL\_TABLE.hql script to create an external table
    
      - CREATE\_MANAGED\_TABLE.hql script to create an external table
    
      - DSTI\_DB.hql script to change the reference database

  - Copy these scripts on the hdfs in a folder, e.g.:
    
      - hdfs dfs -put CREATE\_EXTERNAL\_TABLE.hql oozie-test/firstTest

  - Create a workflow.xml script that has indeed one action-section for
    each of the steps to be executed which are:
    
      - Run DSTI\_DB.hql to select the desired database
    
      - Run CREATE\_EXTERNAL\_TABLE.hql
    
      - Run CREATE\_EXTERNAL\_TABLE.hql
        
        You have to make sure that each action-sections:
    
      - Points to the proper hql script path in the tag \<script\>,
        e.g.:
        
          - \<script\>oozie-test/firstTest/DSTI\_DB.hql\</script\>
    
      - points to the subsequent section upon successful execution –
        this can be done via the tag
        
          - \<ok to = "create\_external\_csv\_table"/\>

  - Copy the workflow.xml on hdfs

  - Create in the edge node a job.properties file which:
    
      - Points to the workflow.xml path on hdfs
    
      - With the proper connection details to Yarn and the Hive server
        
        Please refer to the attached job.properties example for more
        details

  - Run the below command from the edge node:
    
      - oozie job -oozie http://oozie-1.provider.cloud:11000/oozie
        -config job.properties -run
