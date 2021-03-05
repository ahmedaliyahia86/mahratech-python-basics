# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:58:42 2020

@author: ahmedali
"""
# 1- print() Function

# Displays the string value inside the parentheses on the screen

print('Hello World!')

print(12)

# 2- input() Function

# Pauses your program and waits for the user to Enter some text

# Takes one argument : the prompt, or instructions, that we want to display
# to the user so they know what to do.

# Always returns to a string

input()

x=input('Enter an integer : ')
print(x)
print(type(x))

# Use the int() code to convert string value to an integer one

x=int(input('Enter an integer : '))
print(x)
print(type(x))