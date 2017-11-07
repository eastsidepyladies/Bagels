#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:09:49 2017

@author: rimikamajumdar
"""

# importing the libraries
import random

num = [0,1,2,3,4,5,6,7,8,9]
numbers = random.sample(range(10), 3)
print(int(''.join(map(str,numbers))))

def get_random_number():
    numbers = random.sample(range(10), 3)
    number = ''.join(map(str,numbers))
    return number

def main():
    print("I am thinking of a 3-digit number. Try to guess what it is")
    print("Here are some clues")
    print("When I say:\tThat means:")
    print("Pico".rjust(6) + "\t\tOne digit is correct but in the wrong position.")
    print("Fermi".rjust(6) + "\t\tOne digit is correct and in the right position")
    print("Bagels".rjust(6) + "\t\tNo digit is correct")
    
    number = get_random_number()
    print("I have thought up a number. You have 10 guesses to get it")
    
if __name__ == "__main__": main()
