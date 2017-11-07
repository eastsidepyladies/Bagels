#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:09:49 2017

@author: rimikamajumdar
"""

# importing the libraries
import random

# returns "yes" or "no" for whether user wants to play again
def another_game():
    play = input("Do you want to play Bagels again? (yes or no):\n")
    if play.lower() == "yes":
        return "yes"
    else:
        return "no"
        

# returns string to the user with a clue or
# winning note
# the clue order is randomized
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


# returns true if the user's guess is a 3 digit number and false otherwise
def valid_number(guess):
    nums = '0 1 2 3 4 5 6 7 8 9'.split()
    if guess == "":
        return False
    for i in guess:
        if i not in nums:
            return False
    return True
    
# returns a three digit number, with unique random digits
def get_random_number():
    numbers_array = random.sample(range(10), 3)
    number = ''.join(map(str,numbers))
    return number


def main():
    user = 0
    comp = 0
    play = "yes"
    while play == "yes":
        print("I am thinking of a 3-digit number. Try to guess what it is")
        print("Here are some clues")
        print("When I say:\tThat means:")
        print("Pico".rjust(6) + "\t\t1 digit is correct but in the wrong position.")
        print("Fermi".rjust(6) + "\t\t1 digit is correct and in the right position")
        print("Bagels".rjust(6) + "\t\tNo digit is correct")
        
        number = get_random_number()
        print("I have thought up a number. You have 10 guesses to get it")
        for i in range(1,11):
            guess = input("Guess #" + str(i) + ":\n")
            if valid_number(guess):
                # compare user's guess with random number and return a clue
                clue = compare_numbers(guess,number)
                print(clue)
                # if user guesses correct number, the for loop breaks
                if clue =="You win! Congrats!":
                    user+=1
                    print("Your points: " + str(user) + " Computer's points: " + str(comp))
                    break
                
            else:
                print ("Invalid input.. Try Again")
                if i == 10:
                    comp+=1
                    print("Haha! You lose!")
                    print("Your points: " + str(user) + " Computer's points: " + str(comp))
                
        play = another_game()
        
    
if __name__ == "__main__": main()
