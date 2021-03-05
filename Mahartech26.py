# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 05:02:24 2020

@author: ahmedali
"""

# Python Collections : 3- Dictionaries

# 3- Dictionaries: 1- Creating a Dictionary

my_dict = {}     # Initiating Empty Dictionary
print(my_dict)

# Examples: 

grades = {'Ana':'B', 'John':'A+', 'Denise':'A'}

print(grades)

G = grades['Ana']

print(G)
print(type(G))

print('----------------------')

dic = {'Hussam':'A+', 'Mahmoud':'B-', 'Nahed':'A'}

print(dic)

# 3- Dictionaries: 2- Adding New Entry (Key-Value Pairs)

dic['Dina'] = 'C'

print(dic)

# The in and not in Operators work on the Keys

print('Hussam' in dic)

print('hussam' in dic)

print('----------------------')

# 3- Dictionaries: 3- Removing an Entry (Key-Value Pairs) 

del[dic['Mahmoud']]

print(dic)

print('----------------------')


# 3- Dictionaries: 4- .keys() and .values() Methods

# * .keys() : Get an Iterable that acts like a Tuple of all keys
 
# * .values() : Get an Iterable that acts like a Tuple of all values

K = dic.keys()

V = dic.values()

print(K)

print(V)

print(type(K))

print(type(V))



















