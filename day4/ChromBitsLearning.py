#!/usr/bin/env python
import ChromBits as cb
import sys

arr = cb.ChromosomeLocationBitArrays (fname= sys.argv[1])

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file(fname=sys.argv[2]) 
beaf.set_bits_from_file(fname=sys.argv[3])

ctcf.intersect(beaf)


new = beaf.intersect( ctcf.complement())
thing = new.collapse()
print thing
#Length = arrays_from_the_len_file (sys.argv[1])

#set_bits_from_file( Length, sys.argv[2])
#set_bits_from_file( Length, sys.argv[3])
