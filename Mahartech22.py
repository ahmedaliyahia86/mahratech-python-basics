# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:33:00 2020

@author: ahmedali
"""

# Python Collections: 2- Lists

# 1- Lists: Defining a List

# * Denoted by Square Brackets, [] , Ex: a =[] empty list
# * Can Contain mixed types, Ex: b =[2, 'c', 4, True]
# * Can (Prefer) Contain Homogenous Elements, Ex: L = [1, 2, 3] : List of Strings, List of Integers ...
# * Lists are mutable, so assigning to an element at an index changes the value

# 1- Creating a List:

L = [1, 2, 3]

print(L)
print(type(L))
L[2] = 5
print(L)

print('-----------------------------')

# 2- Adding an Element to a List with append()

#    .append(x) : Add an item to the end of the list

L.append(7)

print(L)

print('-----------------------------')

# 3- Adding Elements to a List with extend([])

#    .extend(list) : append all the items from a list

L.extend([8, 9])

print(L)

print('-----------------------------')

# 4- Removing Elements from Lists by index with del([])

#    del(L[index]) : delete element at a specific index v

del(L[2])

print(L)

print('-----------------------------')

# 5- Removing Elements from Lists by value with remove()

#   .remove():

#   * remove a specific element -value-
#   * if element occur multiple times, removes first occurence
#   * raises a ValueError if there is no such item

L.remove(8)

print(L)

L.extend([5, 9])

print(L)

L.remove(9)

print(L)

# L.remove(3)              ValueError: list.remove(x): x not in list

print('-----------------------------')

# 6- Removing Elements from Lists with pop()

#    .pop() : removes and returns the last item in the lisL

L.pop()

print(L)

x = L.pop()

print(x)
print(L)

#    .pop(x) : removes an item at any position by including the index of the item

print(L.pop(1))

print(L)


