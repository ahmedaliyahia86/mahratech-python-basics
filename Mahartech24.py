# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:48:18 2020

@author: ahmedali
"""

# Python Collections: 2- Lists

# 13- Lists in Memory:

# ** Storing in both different locations:

L1 = [1, 2, 3]

L2 = [1, 2, 3]

print(L1)
print(L2)

print('-------------------------------')

# ** Alias:

L1 = [4, 5, 6]

L2 = L1

L1[1] = 10

print(L1)
print(L2)      # L1, L2 assignments same memory locations

L2[2] = 0

print(L2)
print(L1)

print('-------------------------------')

# ** Cloning a List:

L1 = [10, 20, 30]

L2 = L1[:]

print(L1)
print(L2)

L2[0] = 99

print(L1)
print(L2)         # Both Assignments for Different Locations

print('-------------------------------')

# ** Sorting a List: Calling sort()

L1 = [5, -2, 10]

L2 = L1.sort()

print(L1)
print(L2)

print('-------------------------------')

# ** Sorting a List : Calling sorted()

L1 = [5, -2, 10]

L2 = sorted(L1)

print(L1)
print(L2)

print('-------------------------------')












