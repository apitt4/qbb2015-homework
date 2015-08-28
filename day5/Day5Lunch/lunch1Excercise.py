#!/usr/bin/env python
import sys
        
reader = open("blastnoutput.txt")

   

for line in reader.readlines(): 
    if line.startswith(">"):
        print line.rstrip("\r\n")
    elif line.startswith(" Identities"):
        fields = line.split(",")
        print fields [0]
        print fields [1]
    else:
        pass


print reader.readline()