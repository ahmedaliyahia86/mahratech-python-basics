# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:52:31 2020

@author: ahmedali
"""
# Python Collections: 2- Lists

# 14- Mutation & Iteration in Lists :

# Example 1: Introduction

def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4,5]
L2 = [2,3]
remove_dups(L1, L2)
print(L1)            # It is not Required
print(L2)

print('-----------------')

# Example 2: Making a Copy of List (Cloning a List)

L1 = [1,2,3,4,5]

def remove_dups(L1,L2):
    L1_Compy = L1[:]
    for e in L1_Compy:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4,5]
L2 = [2,3]
remove_dups(L1, L2)
print(L1)
print(L2)
