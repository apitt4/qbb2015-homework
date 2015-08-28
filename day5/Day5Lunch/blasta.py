#!/usr/bin/env python

class BLASTReader(object):
    def __init__(self, file):
        self.file = file
        self.last_ident = None
        
    def next (self):    
        if  self.last_ident is None: 
            line = self.file.readline()
            assert line.startswith(">"), "Not valid dasta"
            ident = line[1:].rstrip("\r\n")

            #^^^^^^ strip any new line character from the end of the line, remove and return a new line
        else:
            ident = self.last_ident
            
        sequences = []
        while True:
            line = self.file.readline()
            if not line:
                break
            if line.startswith(">"):
                self.last_ident = line[1:].rstrip("\r\n")
                break
            else:
                sequences.append(line.strip()) #remove white space from front and back of the sequence. strip only does left and right \r and \l    
        if len(sequences) == 0:
            raise StopIteration
            
        
        sequences = "".join(sequences) #takes a list of strings and adds them using whatever is before (in this case "")as separaters
        return ident, sequences
        
# all we need to make this iterater is a code that says I'm an iterable and I meet your requirement - there must be an obeject, that returns another object that you call next.
    def __iter__( self ):
        return self