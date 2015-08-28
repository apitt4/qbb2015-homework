#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import pandas as pd


#plt.style.use('ggplot')

data = pd.read_table(sys.stdin, names = ["Score"])
data["Score"].hist()
plt.savefig(sys.argv[1])
