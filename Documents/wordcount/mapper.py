import sys

# for each item in the stdin - in this case each item is a line of a file
for line in sys.stdin:

        line.strip()

        #split the item based on blanck space or tab or newline
        listWord = line.split()

        for word in listWord:

                #return a tuple where the key is the word
                print "%s\t%s" % (word, 1)
