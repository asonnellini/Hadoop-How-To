# How to create a table on HBase

## Overview

In this tutorial I will show how to create a table on HBase, insert a
record and enable versioning.

## Steps

  - Connect to the Edge node

  - Run
    
      - hbase shell

  - Create a Hbase table with a according to the following syntax:
    
      - create 'namespace:table', 'col\_fam1', 'col\_fam2'

![](.//media/image1.png)

  - Check table attributes – by default you see Versioning is disabled
    
      - describe 'dsti\_2020\_fall\_1:sonne\_imdb'
        
        From the below screenshot we can see that by default each family
        column have versioning equal to 1

![](.//media/image2.png)

  - Insert some data
    
      - put ’\<table name\>’,’row1’,’\<colfamily:colname\>’,’\<value\>’

  - Note: when you insert a number, for HBase that is going to be only
    binary data
    
      - hbase(main):005:0\> put
        'dsti\_2020\_fall\_1:sonne\_imdb','and-pulp','opinion:rating','5'
    
      - hbase(main):006:0\> put
        'dsti\_2020\_fall\_1:sonne\_imdb','and-pulp','opinion:comment','Great
        Movie'
    
      - hbase(main):007:0\> put
        'dsti\_2020\_fall\_1:sonne\_imdb','and-pulp','metadata:UserBorn','19861213'
    
      - hbase(main):008:0\> put
        'dsti\_2020\_fall\_1:sonne\_imdb','and-pulp','metadata:UserLang','eng'

  - To check the full content of a table you can use scan **– of course
    in general it is strongly deprecated to use scan because the size of
    the table might be big**

scan 'dsti\_2020\_fall\_1:sonne\_imdb'

![](.//media/image3.png)

  - if you insert a new value for a field of a record that already
    exists (i.e. you use an already existing key, colfam and col name),
    with no versioning enabled, then the previous record will be lost

  - To enable versioning on one family column
    
      - alter 'dsti\_2020\_fall\_1:sonne\_imdb', NAME =\> 'metadata',
        VERSIONS =\> 3

  - Then upon putting a new values for the same record and column
    UserLang and rerunning scan we can see the various versions

![](.//media/image4.png)

  - To select a specific record we can use “get”

![](.//media/image5.png)
