#!/usr/bin/env python

from __future__ import division
from matplotlib_venn import venn3
import numpy as np
import sys

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
        

"""CTCF = set_bits_from_file( Length, sys.argv[2] )
BEAF = set_bits_from_file( Length, sys.argv[3] )
SuHW = set_bits_from_file( Length, sys.argv[4] )    """


##testing new function set_bit

#for key, value in arrays.iteritems():
    #print key, type (value), value.shape, np.sum(value)


CBtotal = 0
CBany_overlap = 0
CBall_overlap = 0
CBhalf_overlap = 0
    
for line in open (sys.argv[2]):
    fields= line.split()
    #define each column/field
    chrom = fields[0]
    start = int (fields [1])
    end = int (fields [2])
    #Get Slice
    sl = BEAF[chrom][start:end] 
    #add
    CBtotal += 1
    #any will tell us if any position in an array is true (1)
    CBany_overlap += sl.any()
    #.all looks at every position in the array and if they are all true return 1 and if not return 0
    CBall_overlap += sl.all()
    #. 50% of a region is overlapped
    CBhalf_overlap += (np.sum(sl)/ len(sl) > 0.5 )
print "CB-total: %d, CB-any overlap: %d, CB-all overlap: %d, CB-Half overlap: %d" % (CBtotal, CBany_overlap, CBall_overlap, CBhalf_overlap)

BStotal = 0
BSany_overlap = 0
BSall_overlap = 0
BShalf_overlap = 0

for line in open (sys.argv[3]):
    fields= line.split()
    #define each column/field
    chrom = fields[0]
    start = int (fields [1])
    end = int (fields [2])
    #Get Slice
    sl = SuHW[chrom][start:end] 
    #add
    BStotal += 1
    #any will tell us if any position in an array is true (1)
    BSany_overlap += sl.any()
    #.all looks at every position in the array and if they are all true return 1 and if not return 0
    BSall_overlap += sl.all()
    #. 50% of a region is overlapped
    #BShalf_overlap += (np.sum(sl)/ len(sl) > 0.5 )
print "BS-total: %d, BS-any overlap: %d, BS-all overlap: %d, BS-Half overlap: %d" % (BStotal, BSany_overlap, BSall_overlap, BShalf_overlap)    

SCtotal = 0
SCany_overlap = 0
SCall_overlap = 0
SChalf_overlap = 0
    
for line in open (sys.argv[4]):
    fields= line.split()
    #define each column/field
    chrom = fields[0]
    start = int (fields [1])
    end = int (fields [2])
    #Get Slice
    sl = CTCF[chrom][start:end] 
    #add
    SCtotal += 1
    #any will tell us if any position in an array is true (1)
    SCany_overlap += sl.any()
    #.all looks at every position in the array and if they are all true return 1 and if not return 0
    SCall_overlap += sl.all()
    #. 50% of a region is overlapped
    SChalf_overlap += (np.sum(sl)/ len(sl) > 0.5 )
print "SC-total: %d, SC-any overlap: %d, SC-all overlap: %d, SC-Half overlap: %d" % (SCtotal, SCany_overlap, SCall_overlap, SChalf_overlap)

SBCtotal = 0
SBCany_overlap = 0
SBCall_overlap = 0
SBChalf_overlap = 0

for line in open (sys.argv[4]):
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
    SBCtotal += 1
    #any will tell us if any position in an array is true (1)
    SBCany_overlap += (sl&sl2&sl3).any()
    #.all looks at every position in the array and if they are all true return 1 and if not return 0
    SBCall_overlap += (sl&sl2&sl3).all()
    #. 50% of a region is overlapped
    SBChalf_overlap += (np.sum(sl&sl2&sl3)/ len(sl&sl2&sl3) > 0.5 )
print "SBC-total: %d, SBC-any overlap: %d, SBC-all overlap: %d, SBC-Half overlap: %d" % (SBCtotal, SBCany_overlap, SBCall_overlap, SBChalf_overlap)

# %d is for inputing integer of decimal, %s input a string %f input float

    