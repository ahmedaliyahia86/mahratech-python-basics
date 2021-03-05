# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:13:34 2020

@author: ahmedali
"""

# Bisection Search Algorithm

print('Please Think of a Number between 0 and 100!')
low = 0
high = 101
medium = (low+high)//2
state = True
while state:
    print('Is Your Secret Number'+str(medium))
    guess = input("Enter 'h' to indicate the guess is too high and Enter 'l' to indicate the guess is too low. Enter 'c' if the answer is guessed correctly")
    if guess=='c':
        print('Game over. Your secret number was : '+str(medium))
        state = False
    elif guess=='h':
        high = medium
        medium = (high+low)//2
    elif guess=='l':
        low = medium
        medium = (high+low)//2
    else:
        print('I did not understand your input')
        