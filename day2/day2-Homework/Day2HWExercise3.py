#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie"


for x in (893, 894, 895, 896, 897, 899, 901,903,905,906, 907,908,909,911, 913,915):
    df = pd.read_csv(annotation+"/SRR072"+str(x)+"/t_data.ctab", comment='#', header=None, sep='\t') 

df.columns = ["id","chromosome","strand","start","end","name", "exon number","length","gene id","gene name","cov","FPKM"]

roi = df["name"].str.contains("FBtr0331261")

print df[roi]
    