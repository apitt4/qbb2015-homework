#!/usr/bin/env python

#How to find the file name

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
#VVVV we can use argv (a list of argument values passed to program)
import sys

#print sys.argv
#How to open a file
#filename = sys.argv[1]


#f = open ( filename )


#line_count =0 initilizes line count to 0
#line_count = 0
#How to read line by line
#Note files can be used in a for loop
#mlinesis just a random variable because when looping a file it automatically reads line by line

#how to print out only lines 10-15
#for lines in f:
#instead of line count you can use enumerate, it works as line_count+=1 and linecount = 0 in this case

#for line_count, lines in enumerate ( f ):
    #if line_count <= 10:
        #pass 
#pass here prevents from going to second
    #elif line_count <= 15:
        #print lines,
    #else: 
        #break
#break out of the for loop, means stop executing a particulr function
#This says no matter what you increase the counter
    #line_count +=1  
    
#instead of line count you can use enumerate

#How to only print columns with a particular phrase    
#Split breaks up a string on whitespace
    #fields = lines.split()
#Split breaks up a string on whitespace
#[9] specifies  colomn    
    #if "tRNA" in fields[9]:
        #print lines, 
#The comma gets rid of the extra line


#Read line gives you all of the files as a list


#Finding gene name and counting for it

#Making a dictionary with name counts
#VVV ????
f = sys.stdin
name_counts = {}


for line_count, lines in enumerate ( f ):
    fields = lines.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[ gene_name ] = 1
    else:
        name_counts[ gene_name ] +=1
#Iterate key, value pairs from the name counts dictionary  --- directional to go through each dictionary line       
for key, value in name_counts.iteritems():
    # Print gene name and count
    print key, value