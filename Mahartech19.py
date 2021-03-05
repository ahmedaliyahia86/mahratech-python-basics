# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:20:17 2020

@author: ahmedali
"""

# Variable Scope Examples:

# Ex1:
def f(y):
    x = 1
    x+=1
    print(x)
x=5
f(x)
print(x)
print('-----------------')
# Ex2:
def g(y):
    print(x)
    print(x+1)
z=5
g(x)
print(x)
print('-----------------')
# Ex3:
x = 5
def h(y):
    x = x+1
    print(x)

#h(x)   # UnboundLocalError: local variable 'x' referenced before assignment
print('-----------------')
# Ex4:
def g(y):
    y = y+x
    print(y)
g(x)