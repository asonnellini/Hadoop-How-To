# Overview

In this tutorial I will show the steps needed to create a very simple
pipeline that is able to import data from a csv file and store it in a
HIVE table that relies on an OCV file stored on the HDFS.

## Assumptions

I will assume that:

  - The csv file name is drivers.csv and is already on the Edge Node

  - **beeline** client is installed on the Edge Node

  - We have access to a Hive Database named dsti\_2020\_fall\_1 on the Hadoop
    Platform

# Steps

  - Connect to the Edge Node

  - Check the content of the csv file, and in
    particular if there is a header and what is the datatype of each
    entry

![](.//media/image1.png)

  - Remove the first line of the file that corresponds to the header;
    for example, I copied the original file drivers.csv to a new file
    drivers\_noheader.csv and then run
    
    This step is needed to ensure that when importing data to the Hive
    tables, the header is not imported
    
    ```
    
    sed -i 1d drivers\_noheader.csv
    
    ```

  - Create the proper External Table in Hive:
    
      - Connect to beeline:
        
        ```
        
        beeline -u
        "jdbc:hive2://zoo-1.au.adaltas.cloud:2181,zoo-2.au.adaltas.cloud:2181,zoo-3.au.adaltas.cloud:2181/dsti;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2;"
        
        ```
    
      - Connect to the database (remember the semi-column\!)
        
        ```
        
        use dsti\_2020\_fall\_1;
        
        ```
    
      - Run the following query to create a table named
        Sonne\_drivers\_csv that is linked to the csv files stored in
        the HDFS location data/drivers.
        
        Remember to end the SQL statement with a semicolumn
        
        Note: this table is going to be “in synch” with the csv files in
        the folder data/drivers:
        
          - if you remove csv files from the folder, the table will not
            show any data;
        
          - if you add a csv file to the folder, the new data will be
            imported
            
            Query:
            
            ```
            
            CREATE EXTERNAL TABLE IF NOT EXISTS Sonne\_drivers\_csv
            (driverId int, name string, ssn integer, location string,
            certified string, wageplan string) ROW FORMAT DELIMITED
            FIELDS TERMINATED BY "," STORED AS TEXTFILE LOCATION
            "data/drivers";
            
            ```
    
      - Check whether the table was created correctly running a simple
        select command
        
        ```SELECT \* FROM sonne\_drivers\_csv LIMIT 3;```

![](.//media/image2.png)

  - Create a managed orc table named Sonne\_drivers\_orc running the
    below SQL statement:
    
    ```
    
    CREATE TABLE IF NOT EXISTS Sonne\_drivers\_orc(driverId int, name
    string, ssn integer, location string, certified string, wageplan
    string) COMMENT 'Data about drivers from a public database' ROW
    FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS ORC;
    
    ```

  - Import in the orc table the data from the csv table
    
    ```
    
    INSERT OVERWRITE TABLE Sonne\_drivers\_orc SELECT \* FROM
    Sonne\_drivers\_csv;
    
    ```

  - To check whether the table is populated, rather than writing
    directly the SQL Select directly on the beeline client, we can
    create on the edge node a text file with the following SQL
    statement:
    
    ```
    
    SELECT \* FROM sonne\_drivers\_orc LIMIT 3;
    
    ```
    
    And then run the script on beeline:
    
    ```
    
    \!run /home/s.andrea-dsti/dataEdge/HiveExercise/select\_query.txt
    
    ```
    
    Where the above is path on the Edge Node to select\_query.txt

![](.//media/image3.png)
