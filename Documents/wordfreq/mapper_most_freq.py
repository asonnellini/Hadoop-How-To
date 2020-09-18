import sys

for line in sys.stdin:

        line.strip()

        word, count = line.split()

        #add a key "mostFreq" to ensure all tuples outputted by this mapper will be processed by the same reducer
        print "%s\t%s\t%s" % ("mostFreq", word, count)