import sys

#stores the word from the previous tuple compared to the tuple being currently processed
previousWord = None

#stores the
previousCount = None

# note here you will receive something like " word \t 1"
for word in sys.stdin:

        keyword, count  = word.split("\t")

        # step to be performed only once, only for the very first tuple
        if previousWord is None:
                previousWord = keyword
                previousCount = 1

        # steps to be performed only from the second tuple onwards
        else:

                #if the word from the new tuple matches the one stored in previousWord
                #then we should increment the counter
                if keyword == previousWord:
                        previousCount = previousCount + 1

                #if the word from the new tuple does not matches the one stored in previousWord
                #then we should consider it as brand new
                else:
                        print "%s\t%s" % (previousWord, previousCount)

                        previousWord = keyword
                        previousCount = 1

#print the last word
print "%s\t%s" % (previousWord, previousCount)
