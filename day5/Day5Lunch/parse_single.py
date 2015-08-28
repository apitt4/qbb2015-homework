#!/usr/bin/env python

"""Parsing a single FASTA record from stdin and print it"""
import sys
from fasta import FASTAReader
        
reader = FASTAReader(sys.stdin)

for i, (ident, seq) in enumerate ( reader ): 
    print i, ident, seq