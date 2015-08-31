#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/Part3.sam"

#How to open a file
f = open ( filename )


#line_count = 0

"""for lines in (f):
    if "NH:i:1" in lines:
        line_count +=1
    else:
        pass"""

for linenum, lines in enumerate(f):
    fields = lines.split()
    chromosomes = fields [1]
    if linenum <= 9:
        print chromosomes
    else:
        break

        

    
  


"""
For the first 10 alignments, print just the column indicating which chromosome a given read aligns to
HINT: .split()
Calculate how many alignments are on chromosome 2L 2R 3L 3R 4 X (keep track separately)
Use a dictionary!
Calculate average MAPQ score
HINT 1: counter and total variables
HINT 2: if you use split() you will need to convert the string to an integer
Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
HINT: and

"""