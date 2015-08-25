#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/Part3.sam"

#How to open a file
f = open ( filename )


line_count = 0
for lines in (f):
    if "NH:i:1" in lines:
        line_count +=1
    else:
        pass
print line_count
