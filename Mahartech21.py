# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:03:30 2020

@author: ahmedali
"""

# 1- Tuples : Tuples Feature

# A- Using a Tuple to Swap Values

x = 5

y = 20

(x,y) = (y,x)

print((x,y))

# B- Return more than value from a function

def quotient_rmainder(x,y):
    q = x//y
    r = x%y
    return (q,r)
z = quotient_rmainder(9,6)
print(z)