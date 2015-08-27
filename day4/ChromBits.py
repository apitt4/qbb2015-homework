from __future__ import division
from matplotlib_venn import venn3
import numpy as np
import sys
import copy
#^^^ it used to always return an integer, changes division to work on floating numbers
"""Creating an array to count the number of intersection in two BED files: for each chromosome create the array of the length that is all zero"""


"""you first create a function (def), then create an empty dictionary named arrays, then you create a loop that for ever line in the file name do the following, the field  command splits the file into
two columns then names the first column 'name' and it names the second column 'size' and also inforces that that line must be an integer then you say for ever line in 'name' transform every unit of the chromosome
into a zero then place that zero into the size column also dtype=bool just means it must be the type zero to be in the array finally use return function. then the second to last 'for key, valueetc.' means for every key (dictionary key in this case is name-- the value would be 0000...(number of chromosome units represented as zero))also the sys.argv[1] opens the second file in your command (your.py is the zeroth file]file and operates the file on that
then finally you print the key 'name', the type of (value 'what type is the stuff located in the size columns), then finally you print the shape of the size column (value) ORR the number of zeroes which in this case indicates the length of the chromosome. the 'for key/print' loop was just a  test and has been commented out"""
class ChromosomeLocationBitArrays (object):

    def __init__ ( self, dicts=None, fname =None ):
        if dicts is not None:
            arrays=dicts
        else:
            arrays = {}
        if fname is not None:
            for line in open ( fname ):
                fields= line.split()
                name = fields[0]
                size = int (fields [1])
                arrays[name] = np.zeros(size, dtype=bool)
            self.arrays = arrays
    
        #for key, value in arrays.iteritems():
            #print key, type (value), value.shape    

        def set_bits_from_file ( self, fname ):
            for line in open ( fname ):
                fields= line.split()
            #define each column/field
                chrom = fields[0]
                start = int (fields [1])
                end = int (fields [2])
                self.arrays[chrom][start:end]= 1 
        #[chrom] looks up the key in the dictionary then for every one that has  the same thing in start:end positions gets changed to 1

        def intersect ( self, other):
            rval = {}
            for chrom in arrays1:
                rval[chrom] = arrays1chrom & arrays2[chrom]
            return ChromosomeLocationBitArrays (dicts=rval)
    
        def union ( self, other):
            rval = {}
            for chrom in self.arrays1:
                rval[chrom] = arrays1[chrom] | arrays2[chrom]
            return ChromosomeLocationBitArrays (dicts=rval)
    
        #everything that was true was false and everything was true is now false    
        def complement ( self ):
            rval = {}
            for chrom in self.arrays1:
                rval[chrom] = ~ self.arrays1[chrom]
            return ChromosomeLocationBitArrays (dicts=rval)
        def copy (self):
            return ChromosomeLocationBitArrays (dicts=copy.deepcopy(self.arrays))
    
