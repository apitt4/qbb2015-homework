#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

#df is a data frame and a bunch of comlumns and a bunch of rows
df = pd.read_table(annotation, comment='#', header=None) 
df.columns = ["chromosome","database","type", "start", "end", "score", "strand", "frame", "attributes"]
roi = df["attributes"].str.contains("Sxl")

roi2 = df["type"].str.contains("transcript")


print df[roi][roi2]
plt.figure()
plt.title("Sxl , transcript only")
plt.plot(df[roi][roi2]["start"])
plt.ylabel("Start Position")
plt.xlabel("gene")
plt.savefig("startsSxltranscript.png")