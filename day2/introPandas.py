#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

#df is a data frame and a bunch of comlumns and a bunch of rows
df = pd.read_table(annotation, comment='#', header=None) 

#print df
#print df.head() -  prints first few rows


#print df.describe() gives a little statiscal information
#print df info() tells you whats integer anf whats an string
#print df[1:5] - prints rows 1,2,3,4 
#print df[10:16] - show rows 10 through 15 (1-based and concluive)

#vvvv adds column names
df.columns = ["Chromosome","database","type", "start", "end", "score", "strand", "frame", "attributes"]


#You can either do it by putting the argument in the order specified on line or put columns="type" or ascending=Falsw
#print df.sort("type", ascending=False)

#print df[["Chromosome","start","end"]] - prints only those columns

#print df["start"][9:15]
#tells you how many rows and columns vvv
#print df.shape 
df2 = df["start"]
#print df2.shape

#df2.to_csv("startColumn.txt", sep='\t', index=False)
#to Search only for a particular phrase in a particular place -- boolean filter
#to find features in annotation for features that are less than 10
#vvvvv works for numeric operations
ROI = df["start"] < 10
print df.shape
print df[ROI]
print ROI.shape
print df[ROI].shape
