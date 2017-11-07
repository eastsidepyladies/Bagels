#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:09:49 2017

@author: rimikamajumdar
"""

# importing the libraries
import random

def valid_number(guess):
    nums = '0 1 2 3 4 5 6 7 8 9'.split()
    if guess == "":
        return False
    for i in guess:
        if i not in nums:
            return False
    return True
    

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
    for i in range(0,13):
        guess = input("Guess #" + i + ": ")
        if valid_number(guess):
            # compare user's guess with random number and return a clue
        else:
            print ("Invalid number.. Try Again")
    
if __name__ == "__main__": main()
