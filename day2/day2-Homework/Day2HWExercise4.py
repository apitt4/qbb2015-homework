#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)
ROI = df["FPKM"] > 0
print df["FPKM"][ROI]
df1= df["FPKM"][ROI]
top =df1[0:3182]
middle= df1[3182:6365]
end= df1[6365:9548]

plt.figure()
plt.title("Excercise 4")
plt.boxplot([top,middle,end])
plt.ylabel("Start Position")
plt.xlabel("gene")
plt.savefig("Exercise4.png")