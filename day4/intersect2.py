#!/usr/bin/env python

from __future__ import division
from matplotlib_venn import venn3
import matplotlib as plt
import numpy as np
import sys
from matplotlib import pyplot as plt


#^^^ it used to always return an integer, changes division to work on floating numbers
"""Creating an array to count the number of intersection in two BED files: for each chromosome create the array of the length that is all zero"""


"""you first create a function (def), then create an empty dictionary named arrays, then you create a loop that for ever line in the file name do the following, the field  command splits the file into
two columns then names the first column 'name' and it names the second column 'size' and also inforces that that line must be an integer then you say for ever line in 'name' transform every unit of the chromosome
into a zero then place that zero into the size column also dtype=bool just means it must be the type zero to be in the array finally use return function. then the second to last 'for key, valueetc.' means for every key (dictionary key in this case is name-- the value would be 0000...(number of chromosome units represented as zero))also the sys.argv[1] opens the second file in your command (your.py is the zeroth file]file and operates the file on that
then finally you print the key 'name', the type of (value 'what type is the stuff located in the size columns), then finally you print the shape of the size column (value) ORR the number of zeroes which in this case indicates the length of the chromosome. the 'for key/print' loop was just a  test and has been commented out"""
def arrays_from_the_len_file ( fname ):
    arrays = {}
    for line in open ( fname ):
        fields= line.split()
        name = fields[0]
        size = int (fields [1])
        arrays[name] = np.zeros(size, dtype=bool)
    return arrays
    
#for key, value in arrays.iteritems():
    #print key, type (value), value.shape    

def set_bits_from_file ( arrays, fname ):
    for line in open ( fname ):
        fields= line.split()
    #define each column/field
        chrom = fields[0]
        start = int (fields [1])
        end = int (fields [2])
        arrays[chrom][start:end]= 1 
#[chrom] looks up the key in the dictionary then for every one that has  the same thing in start:end positions gets changed to 1
    
    
Length = arrays_from_the_len_file (sys.argv[1])

for x in range(2,5):
    Length = arrays_from_the_len_file (sys.argv[1])
    set_bits_from_file( Length, sys.argv[x] )
    if x == 2:
        CTCF = Length
    elif x == 3:
        BEAF = Length
    elif x == 4:
        SuHW = Length

#SBCtotal = 0
Total = 0
SBCany_overlap = 0

#CBtotal = 0
CBany_overlap = 0

#BStotal = 0
BSany_overlap = 0

#SCtotal = 0
SCany_overlap = 0

#Stotal = 0
Sany_overlap = 0

#Btotal = 0
Bany_overlap = 0

#Ctotal = 0
Cany_overlap = 0

for x in sys.argv[2:]:   
    for line in open (x):
        fields= line.split()
        #define each column/field
        chrom = fields[0]
        start = int (fields [1])
        end = int (fields [2])
        #Get Slice
        sl = CTCF[chrom][start:end] 
        sl2 = BEAF[chrom][start:end]
        sl3 = SuHW[chrom][start:end]
        #add
        Total += 1
        #SBCTotal += 1
        #any will tell us if any position in an array is true (1)
        SBCany_overlap += (sl&sl2&sl3).any()
        #.all looks at every position in the array and if they are all true return 1 and if not return 0
        #SBCall_overlap += (sl&sl2&sl3).all()
     
        #CBtotal += 1
        CBany_overlap += (sl&sl2).any()
        
        #BStotal += 1
        BSany_overlap += (sl2&sl3).any()

        #SCtotal += 1
        SCany_overlap += (sl&sl3).any()

        #Stotal += 1
        Sany_overlap += sl3.any()

        #Btotal += 1
        Bany_overlap += sl2.any()

        #Ctotal += 1
        Cany_overlap += sl.any()
        
        
        #. 50% of a region is overlapped
        #SBChalf_overlap += (np.sum(sl&sl2&sl3)/ len(sl&sl2&sl3) > 0.5 )
#print "SBC-total: %d, SBC-any overlap: %d,CB-total: %d, CB-any overlap: %d,BS-total: %d, BS-any overlap: %d,SC-total: %d, SC-any overlap: %d,S-total: %d, S-any overlap: %d,B-total: %d, B-any overlap: %d,C-total: %d, C-any overlap: %d, " % (SBCtotal, SBCany_overlap, CBtotal, CBany_overlap,  BStotal, BSany_overlap, SCtotal, SCany_overlap, Stotal, Sany_overlap, Btotal, Bany_overlap, Ctotal, Cany_overlap)

print "Total: %d, SBC-any overlap: %d, CB-any overlap: %d, BS-any overlap: %d, SC-any overlap: %d, S-any overlap: %d, B-any overlap: %d, C-any overlap: %d, " % (Total, SBCany_overlap, CBany_overlap,  BSany_overlap, SCany_overlap, Sany_overlap, Bany_overlap, Cany_overlap)


NewC = Cany_overlap - ((CBany_overlap + SCany_overlap) - SBCany_overlap) 
print "C - ((CB+SC)-SBC): %d, NewC" % (NewC)

NewB = Bany_overlap - ((CBany_overlap+BSany_overlap) - SBCany_overlap) 
print "B - ((CB+BS)-SBC): %d,NewB " % (NewB)

NewS = Sany_overlap - ((BSany_overlap + SCany_overlap) - SBCany_overlap) 
print "B- ((BS+SC)-SBC): %d, NewS" % (NewS)

NewSC = SCany_overlap - SBCany_overlap 
print "SC-SBC): %d,NewSC " % (NewSC)

NewCB = CBany_overlap - SBCany_overlap
print "CB-SBC: %d, NewCB" % (NewCB)

NewBS = BSany_overlap - SBCany_overlap
print "BS-SBC: %d,NewBS " % (NewBS)
print SBCany_overlap

Total1 = NewC + NewB + NewS + NewSC + NewCB + NewBS + SBCany_overlap
print Total, Total1


venn3(subsets = (NewC, NewB, int(NewSC), NewS, int(NewCB), int(NewBS), int(SBCany_overlap)), set_labels = ('CTCF', 'SuHW', 'BEAF'))

plt.title("Venn Diagram")
plt.savefig("VennDiagram.png")























