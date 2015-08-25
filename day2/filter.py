#!/usr/bin/env python

#How to find the file name

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

#How to open a file
f = open ( filename )

#How to read line by line
#Note files can be used in a for loop
#mlinesis just a random variable because when looping a file it automatically reads line by line
for lines in f:
#Split breaks up a string on whitespace
    fields = lines.split()
#Split breaks up a string on whitespace
#[9] specifies  colomn    
    if "tRNA" in fields[9]:
        print lines, 
#The comma gets rid of the extra line


#Read line gives you all of the files as a list
