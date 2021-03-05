# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:27:44 2020

@author: ahmedali
"""

# for loop .... Controlling loop flow with break

# for var in range(iteration range):
#     statement 1 to be executed
#     if (Condition):
#            break
#     Remaining body for loop

mysum=0
for i in range(5,11,2):
    mysum+=i
    if mysum==8:
        break
print(mysum)