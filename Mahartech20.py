# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:52:23 2020

@author: ahmedali
"""

# Python Collections: 1- Tuples

# 1- Tuples : Defining a Tuple

# * Defined by Parentheses ()
# * Items Separated By Commas ( 1, )
# * Contain any type of object

t=()
print(type(t))
tup = (1, 'C', 3, 'Num')
print(tup)

# 1- Tuples: Retrieving Elements from a Tuple

# * Element access with square brackets and zero-based index, t[index]

print(tup[2])

# 1- Tuples : Concatenating Tuple Content with + Operator

tup2 = tup + (20,13)
print(tup2)  

# 1- Tuples : Slicing on Tuples

#   Note: A tuple must always use a Comma, even if there is only one element

print(tup2[1:2])

x = ('C')
y = ('C',)
print(type(x))
print(type(y))

x1 = 10
x2 = 10,
print(type(x1))
print(type(x2))

# 1- Tuples: Writing on a Tuple

#   Note: Tuples are immutable, values can not change once created

print(tup2)
print(tup2[4])
# tup2[4] = 25              # Error

#   Note: You can only overwrite full tuple

tup2 = ((1, 'C', 3, 'Num', 25, 13))

print(tup2)
