# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:00:26 2020

@author: ahmedali
"""

# Python Collections: 2- Lists

# 7- String Conversion to a List

#  list() : returns a list with every character forms

S = "I <3 CS"         # Meaning: I love Computer Science
x = list(S)
print(x)
print(type(x))

print('-----------------------------')


# 8- Splitting a String to a List

#   .split() : Split a String on a Character Parameter

L1 = S.split('<')

print(L1)

print('-----------------------------')

# 9- Concatenating List into String

#   .join() : Turn a List of Characters into a String

L = ['a', 'b', 'c']

S1 = ''.join(L)
print(S1)

S2 = '_'.join(L)
print(S2)

S3 = '*'.join(L)
print(S3)

print('-----------------------------')

# 10- Sorting a List Temporarily with sorted()

#   sorted(L) : Returns sorted list, does not mutate L

L = [1, 5, -3, 20, 4, 9]
print(sorted(L))
print(L)
x = sorted(L)
print(x)
print(L)

print('-----------------------------')

# 11- Sorting a List Mutately with .sort()

#   L.sort() : Mutate L, sort items in place

L = [1, 5, -3, 20, 4, 9]
L.sort()
print(L)

print('-----------------------------')

# 12- Reversing the list in-place with reverse()

#   L.sreverse() : Reverse the elements of the list in place

L = [1, 5, -3, 20, 4, 9]
L.reverse()
print(L)

# Other List Operations : Very Much

# https://docs.python.org/3/tutorial/datastructures.html
