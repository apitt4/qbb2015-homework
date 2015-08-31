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
    elif fields[2] == ("2L") and int(fields[3]) >= 10000 and int(fields[3])<= 20000:
        counter += 1


print counter




"""

Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
HINT: and"""