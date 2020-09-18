# Overview

In this tutorial I will describe the steps I performed to implement a
map-reduce that count words from a file and returns a list of tuples
where the key is the word and the value is the number of times the word
appears in the text.

Note: for the sake of simplicity we did not normalize words.

## Prerequisites

We assume that:

  - An Hadoop platform is already fully configured and can be accessed
    via an Edge Node.

  - A hadoop-streaming.jar file is available in the platform to be run
    in conjunction with custom mapper.py and reducer.py

# Steps

  - The idea is to write:
    
      - a mapper that parses lines from a text and for each word in the
        text outputs a tuple where they key is the word itself and the
        value is 1 – see for example mapper.py
        
        The same word will then appear multiple times in the set of
        tuples
    
      - reducer that takes in input the tuples produced by the mapper
        and returns a set of tuples where each tuple is made of a key
        equal to the word and a value equal to the number of occurrences - see for example reducer.py

  - Both mapper.py and reducer.py should be placed in the edge node:

![](.//media/image1.png)

  - Place the file with the text to be parsed in an hdfs folder for
    which you have permissions
    
    For example in our case the text file was stored in
    data/wordcount/inputTest.txt

![](.//media/image2.png)

  - In our case the text is:

![](.//media/image3.png)

  - Run the below command ensuring that:
    
      - The option ``` -file ``` point to the mapper.py and
        reducer.py files
    
      - The option ``` -input ``` points to the path of the text
        file on the hdfs
    
      - The option ``` -output ``` points to a folder which does
        not exists yet

```

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
-file mapper.py -mapper "python mapper.py" -file reducer.py -reducer
"python reducer.py" -input data/wordcount/inputTest.txt -output
data/wordcount/output

```

  - Once the command is executed, information about its execution are
    displayed

  - The final output of the reducer is by default returned in the folder
    pointed by the -output flag of the previous command – in our case it
    was the directory ```data/wordcount/output```

![](.//media/image4.png)

  - That directory contains 2 files:
    
      - \_SUCCESS file that confirms the map-reduce was executed with no
        issues
    
      - A part-0000 file that has the output tuples

![](.//media/image5.png)
