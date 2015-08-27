#!/usr/bin/env python

import chrombits


arr = ChromosomeLocationBitArrays (fname= sys.argv[1])

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file(sys.argv[2])
beaf.set_bits_from_file(sys.arg[3])

new = beaf.intersect( ctcf.intersect())


Length = arrays_from_the_len_file (sys.argv[1])

set_bits_from_file( Length, sys.argv[2])
set_bits_from_file( Length, sys.argv[3])


