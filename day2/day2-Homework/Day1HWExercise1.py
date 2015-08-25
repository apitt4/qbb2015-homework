#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

#df is a data frame and a bunch of comlumns and a bunch of rows
df = pd.read_table(annotation, comment='#', header=None) 
df.columns = ["chromosome","database","type", "start", "end", "score", "strand", "frame", "attributes"]
roi = df["attributes"].str.contains("Sxl")
print df[roi]

plt.figure()
plt.title("Sxl")
plt.plot(df[roi]["start"])
plt.ylabel("Start Position")
plt.xlabel("gene")
plt.savefig("startsSxl.png")