#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:09:49 2017

@author: rimikamajumdar
"""

# importing the libraries
import random

def another_game():
    play = input("Do you want to play Bagels again? (yes or no):\n")
    if play.lower() == "yes":
        return True
    else:
        return False
        

def compare_numbers(guess, number):
    clue = []
    length = len(guess)
    if guess == number:
        return ("You win! Congrats!")
    
    for i in range(length):
        if guess[i] == number[i]:
            clue.append("Fermi")
        elif guess[i] in number:
            clue.append("Pico")
    if len(clue) == 0:
        return ("Bagels")
    
    clue.sort()
    clue_str = ' '.join(clue)
    return clue_str

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
    for i in range(1,11):
        guess = input("Guess #" + str(i) + ": ")
        if valid_number(guess):
            # compare user's guess with random number and return a clue
            clue = compare_numbers(guess,number)
            print(clue)
            if clue =="You win! Congrats!":
                
                break
            
        else:
            print ("Invalid number.. Try Again")
    
if __name__ == "__main__": main()
