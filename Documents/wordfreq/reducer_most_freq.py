import sys

#keep track of the most frequent word scanned so far by the reducer
maxWord = None
#number of counts of the most frequent word
maxCount = 0

for line in sys.stdin:

        commonKey, word, count = line.split("\t")

        #update maxWord and maxCount in case the tuple currently being processed refers to a$
        if count > maxCount:
                maxWord = word
                maxCount = count


print "%s\t%s\t%s" % (commonKey,maxWord, maxCount)
