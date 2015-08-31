#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/Part3.sam"

#How to open a file
f = open ( filename )

line_count = 0
#How to read line by line
#Note files can be used in a for loop
#lines is just a random variable because when looping a file it automatically reads line by line

for lines in ( f ):
    #print lines
    line_count +=1
 
print "This is question 1:"   
print line_count - 1
print


    
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