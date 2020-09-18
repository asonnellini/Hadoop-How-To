# Overview

Following on from the tutorial on map-reduce to count the words from a
text, in this tutorial I will show how to implement a map-reduce that
takes in input the tuples that have the number of occurrences of each
word in a text, and extract the tuple with the highest count.

So we are assuming that the map-reduce of the previous tutorial was
successfully run and printed on hdfs its output on
data/wordcount/output/part-00000.

# Steps

  - Create on the edge node a mapper and reducer python file like
    mapper\_most\_freq.py and reducer\_most\_freq.py attached
    
      - Note: Given that you have to compare multiple tuples, you have
        to ensure they will all be processed by the same reducer. To
        ensure this you have to make sure all the tuples produced by the
        mapping share the same key.
        
        This can be achieved building a mapper that gives in output
        tuples with the same key, while each of their values corresponds
        to the tuple from the previous map-reduce function

![](.//media/image1.png)

  - Run the above new map-reduce taking in input the text file that was
    outputted from the previous map-reduce that counted words

\`\`\`

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
-file mapper\_most\_freq.py -mapper "python mapper\_most\_freq.py" -file
reducer\_most\_freq.py -reducer "python reducer\_most\_freq.py" -input
data/wordcount/output/part-00000 -output data/wordfreq/output

\`\`\`

  - The output file confirms the map-reduce worked:

> ![](.//media/image2.png)
