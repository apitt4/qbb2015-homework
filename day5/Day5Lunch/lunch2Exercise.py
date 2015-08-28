#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

        
reader = open("blastnoutput.txt")

Evalues = []   
Score = []
for line in reader.readlines(): 
    if line.startswith(" Score"):
        fields = line.split()
        print fields[7]
        Score.append(float(fields[2]))
        Evalues.append(float(fields[7]))
        
    else:
        pass
Scorelog = np.log(Score)
plt.figure()
plt.hist(Scorelog)
plt.title("Score Histogram")
plt.xlabel("log(Score)")
plt.ylabel("Count")
plt.savefig("Histogram_Score.png")


Evalueslog = np.log(Evalues)
plt.figure()
plt.hist(Evalueslog)
plt.title("E-values Histogram")
plt.xlabel("log(Evalues)")
plt.ylabel("Count")
plt.savefig("Histogram_Evalues.png")

NeglogEval = -np.log(Evalues)
plt.figure()
plt.scatter(NeglogEval,Score)
plt.xlabel("NeglogEval")
plt.ylabel("Score")
plt.savefig("Scores v E-values.png")