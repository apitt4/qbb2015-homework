#!/usr/bin/env python

import numpy
import numpy.random
import subprocess

def random_sequence():
    return "".join(numpy.random.choice(list("ACGT"), 1000))
    
scores = []

for i in range(5000):
    open("t1.seq","w").write(random_sequence())
    open("t2.seq","w").write(random_sequence())
    out = subprocess.check_output(
    "blastn -task blastn -query t1.seq -subject t2.seq".split())
    
    for line in out.split("\n"):
        if line.strip().startswith("Score ="):
            print line.split()[2]
