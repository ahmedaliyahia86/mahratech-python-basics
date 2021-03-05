# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:25:07 2020

@author: ahmedali
"""

# Nested if Statement
x = int(input('Enter an Integer : '))
if x%2==0:
    if x%3==0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3==0:
    print('Divisible by 3 and not by 2')