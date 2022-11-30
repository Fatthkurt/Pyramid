import math

# Task 1: Write a function to create an upper pyramid
"""
Description: 
# The function takes a parameter "n" which decides the size of the pyramid. 
# The pyramid is constructed out of asterisks (*).
# In other words, "n" decides the number of * at the BASE of the pyramid.
# Your function should INCREASE the number of * from 1 to "n" thereby creating a pyramid.

Further explanation will be given in class :-)
"""

## Your code below:
## -------------------


def upper_pramid(n):
   if n%2==1: 
    a=1
    b= int(n/2)
    c= math.ceil(n/2)
    for element in range(c):
        print (" "*b+"*"*a+" "*b)
        a= a +2
        b= b -1


   elif n%2==0:
    a=2
    b= int(n/2)-1
    c= int(n/2)
    for element in range(c):
        print (" "*b+"*"*a+" "*b)
        a= a +2
        b= b -1


























# Task 2: Write a function to create a lower pyramid
"""
Description: 
# The function takes a parameter "n" which decides the size of the pyramid. 
# The pyramid is constructed out of asterisks (*).
# In other words, "n" decides the number of * at the TOP of the pyramid.
# Your function should REDUCE the number of * from "n" to 1 
thereby creating an INVERTED pyramid.

Further explanation will be given in class :-)
"""

## Your code below:
## -------------------

def lower_pramid(n):
   if n%2==1: 
    a=n
    b= 0
    c= math.ceil(n/2)
    while c >0:
        print (" "*b+"*"*a+" "*b)
        a= a -2
        b= b +1
        c=c-1


   elif n%2==0:
    a=n
    b= 0
    c= int(n/2)
    for element in range(c):
        print (" "*b+"*"*a+" "*b)
        a= a -2
        b= b +1


