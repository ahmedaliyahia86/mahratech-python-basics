# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:21:59 2020

@author: ahmedali
"""
# Four Functions' Types:

# 1- No arguments & No return Function

# Explan.1:

#     def functionName():
#         Function Code

# Ex.1:
def printHello():
    print("We printed this though function with now input parameters or return")

printHello()
print("------------------------------")

# 2- With arguments & No return Function

# Explan.2:

#     def functionName(arguments):
#         Function Code

# Ex.2:
def printSum(num1,num2):
    print(num1+num2)

printSum(5,10)
x = 20
y = 30
printSum(x,y)
print("------------------------------")

# 3- No arguments & With return Function

# Explan.3:

#     def functionName():
#         return value

# Ex.3:
def pi():
    return 22/7

circ = 2 * 7 *pi()
print(circ)
print("------------------------------")

# 4-  With arguments & With return values Function

# Explan.4:

#     def functionName(arguments):
#         return value

# Ex.4:
def isEven(num):
    return num%2==0

isEven(2)
print(isEven(2))
print(isEven(3))

def isOdd(num):
    """ 
This function is used to tell if the given number is odd 
input: Num , Type: Integer 
Output: Boolean
"""
    return num%2!=0
print(isOdd(2))
print(isOdd(3))    
    
print("------------------------------")