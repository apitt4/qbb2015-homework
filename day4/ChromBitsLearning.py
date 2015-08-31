#!/usr/bin/env python
from __future__ import division
import ChromBits as cb
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import sys 


arr = cb.ChromosomeLocationBitArrays (fname= sys.argv[1])

ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()

ctcf.set_bits_from_file(fname=sys.argv[2]) 
beaf.set_bits_from_file(fname=sys.argv[3])
suhw.set_bits_from_file(fname=sys.argv[4])

union = beaf.union( ctcf.union(suhw) )

collapsenew=union.collapse()


SBCtotal = 0
CBtotal = 0
BStotal = 0
SCtotal = 0
Stotal = 0
Btotal = 0
Ctotal = 0


for chrom, start, end in collapsenew:
    #Get Slice
    sl1 = ctcf.arrays[chrom][start:end] 
    sl2 = beaf.arrays[chrom][start:end]
    sl3 = suhw.arrays[chrom][start:end]
    
    
    if sl1.any() and sl2.any() and sl3.any(): #all
        SBCtotal += 1
    elif sl1.any() and sl2.any() and not sl3.any(): #23
        CBtotal += 1
    elif sl1.any() and not sl2.any() and sl3.any():#34
        SCtotal += 1
    elif sl3.any() and sl2.any() and not sl1.any(): #24
        BStotal += 1
    elif sl1.any() and not sl2.any() and not sl3.any(): #2
        Ctotal += 1
    elif sl3.any() and not sl2.any() and not sl1.any(): #3
        Stotal += 1
    else:
        Btotal +=1  #4

   
print "SBC-total: %d,CB-total: %d,BS-total: %d,SC-total: %d, S-total: %d, B-total: %d,C-total: %d " % (SBCtotal, CBtotal,  BStotal,  SCtotal, Stotal,  Btotal, Ctotal)
        

    

plt.figure()
venn3(subsets=(Btotal, Stotal,BStotal,Ctotal,CBtotal,SCtotal,SBCtotal), set_labels = ('SuHW','CTCF','BEAF'))
plt.savefig("Venn2.png")


