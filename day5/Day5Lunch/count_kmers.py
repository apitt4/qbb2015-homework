#!/usr/bin/env python

"""Count kmers in fasta file"""
import sys
from fasta import FASTAReader

reader = FASTAReader(sys.stdin)
counts = {}
k = 11

for ident, sequence in reader:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer not in counts:
            counts[kmer] = 1
        else: 
            counts[kmer] +=1



#for key in counts:
    #print key, counts[key]
    
#To sort
for key in sorted(counts, key =counts.get):
    print key, counts[key]