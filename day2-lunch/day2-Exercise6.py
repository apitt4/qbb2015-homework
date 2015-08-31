#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/Part3.sam"

#How to open a file
f = open ( filename )
counter = 0
total = 0
for line in f:
    fields = line.split()
    if "@" in line:
        pass
    else:
        fields = line.split()
        counter += 1
        total += int(fields[4])
avg = total/counter

print avg




"""Calculate average MAPQ score
HINT 1: counter and total variables
HINT 2: if you use split() you will need to convert the string to an integer
Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
HINT: and"""