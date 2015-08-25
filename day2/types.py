#!/usr/bin/env python

# Integer
#Python has no upper limit on python size
i = 1000000

# Floating point / real number
f =0.3333

#To make an integer a floating point

i_as_f = float( i )
f_as_i = int(f) 


#Spaces around operating signs (+, -, = etc.)
# White space is 4 spaces

#Lists use [] -- convention contains only on type ie. all integers, all floating points etc.
l = [1,2,3,4,5]
#something exclusive to lists but not tuples
l.append(7 )

#Tuples use ()
#Tuples aren't modifiable by something like t.append
t = (1, "foo", 5.0)
#String can be double quote or single
s = "A String"
s = 'A String'

#Boolean
truthy = True
falsy = False

#Dictionary
d1 = {"key1": ["lions","tigers", "cows"], "key2" : "value2"}
#You can pass a list using dict function
d2 = dict( key1="value1", key2= "value2")
d3 = dict( [ ("key1","value1"),("key2", "value2") ] )

for value in ( i, f, s, truthy, l, t, d1, d2, d3 ):
    print value, type ( value )