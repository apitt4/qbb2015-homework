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
            counts[kmer] = [ (ident, i) ]
        else: 
            counts[kmer].append(i) 

query = sys.argv[1]

for i in range(0, len(query) - k):
    kmer = query[i:i+k]
    if kmer in counts:
        matches = counts[kmer]
        for ident, pos in matches:
            print i, pos, ident

#for key in counts:
    #print key, counts[key]
    
#To sort