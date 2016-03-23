#!/usr/bin/env python  

import sys  
  
# input comes from STDIN (standard input)  
for line in sys.stdin:  
    # remove leading and trailing whitespace  
    line = line.strip()  
    # split the line into words  
    temp = line.split('\t')
    oalist = temp[1]
    # increase counters  
    oalist = oalist.split(',')
    for i in range(len(oalist)):
        for j in range(len(oalist)):
            print '%s\t%s\t%s' % (oalist[i], oalist[j], 1)
    # for word in words:  
    #     # write the results to STDOUT (standard output);  
    #     # what we output here will be the input for the  
    #     # Reduce step, i.e. the input for reducer.py  
    #     #  
    #     # tab-delimited; the trivial word count is 1  
    #     print '%s\t%s' % (word, 1)  