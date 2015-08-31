#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/Part3.sam"

#How to open a file
f = open ( filename )

dic = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}

for line in f:
    fields = line.split()
    if "@" in line:
        pass
    elif fields[4] in dic:
        dic[(fields[4])] += 1 
        #print fields[1]    
for key, value in dic.items():
    print key, value 





"""Calculate how many alignments are on chromosome 2L 2R 3L 3R 4 X (keep track separately)
Use a dictionary!
Calculate average MAPQ score
HINT 1: counter and total variables
HINT 2: if you use split() you will need to convert the string to an integer
Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
HINT: and"""