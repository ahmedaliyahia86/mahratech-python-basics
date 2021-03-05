# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 05:48:50 2020

@author: ahmedali
"""

# Python Collections : 3- Dictionaries

# 3- Dictionaries : Dictionary Operations

d1 = {'A':10, 'B':20}

print(d1)

print('-------------------------')

# * Dictionary Operations : 1- Iterating Through a Dictionary

print('-------------------------')

for key in d1:
    print(key+':'+str(d1[key]))

# * Dictionary Operations : 2- Modifying Values

d2 = {'C':30, 'D':40}

d1['A'] = 100

print(d1)

print('-------------------------')


# * Dictionary Operations : 3- get() Method

print(d1.get('A'))

#print(d1['F'])        # KeyError

x = d1.get('F')

print(x)

y = d1.get('F', -1)

print(y)

print(d1)

print('-------------------------')

# * Dictionary Operations : 4- Updating a Dictionary

d1['F'] = 90

print(d1)
print(d2)
d1.update(d2)

print(d1)             # Addong a Dictionary to another



















