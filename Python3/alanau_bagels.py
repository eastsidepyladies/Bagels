#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-11-09'

# Bagels: a guessing game 
#
# The game will generate a 3-digit non-repeating number from digits 0-9.
# - 'Fermi'  = correct digit in proper place
# - 'Pico'   = correct digit in wrong place
# - 'Bagels' = no correct digits

import random  # for sample
from string import digits as digits  # saves me some typing

# random number generator, returns a list of 3 non-repeating digits
def generate_secret():
    numbers = list(map(int,digits))   # seed it with 0-9
    return(random.sample(numbers,3))  # return a list of 3 random selections

# helper function to convert string to a list of integers
def guess_to_list(str_guess):
    list_guess = []
    for str_digit in str_guess:
        list_guess.append(int(str_digit))
    return(list_guess)

# test guess vs. secret (both are lists) and return fermis/picos/bagels (str)
def guess(guess, secret):
    fermi = pico = 0
    output = []
    
    for index in range(len(guess)):
        digit = guess[index]
        if digit==secret[index]:  # this digit is in the right spot
            fermi += 1
        elif digit in secret:  # this digit is correct but in the wrong spot
            pico += 1

    for f in range(fermi):
        output.append("Fermi") 
    for p in range(pico):
        output.append("Pico")
    if output==[]: # no Picos or Fermis, so return Bagels
        output.append("Bagels")
    return(" ".join(output))

# Here's a wrapper to run the game:
def bagels():
    greeting = "Welcome to Bagels! Type 'help' for instructions."
    help_text = """The game will generate a 3-digit non-repeating number.
  'Fermi'  = correct digit in proper place
  'Pico'   = correct digit in wrong place
  'Bagels' = no correct digits

Other commands: hint, answer, exit/quit"""
    
    print(greeting, flush=True)  # this is *supposed* to print first but doesn't always
    
    secret = generate_secret()
    done = play_again = False
    hint = []
    count = 0
    
    while not done:
        print(flush=True)
        str_guess = input("Please guess a number: ").lower()
        if str_guess=="answer":
            print("The answer is:", "".join(list(map(str,secret))))
            play_again = True
        elif str_guess=="quit" or str_guess=="exit":
            done = True
            continue  # exit immediately
        elif str_guess=="hint":
            if len(hint) > 0:
                print("You know it doesn't contain these numbers:", " ".join(list(map(str,hint))))
            else:
                print("You don't have any confirmed information yet. Make more guesses!")
        elif str_guess=="help":
            print(help_text)
        else:
            try:
                int_guess=int(str_guess)
            except ValueError:  # if not an integer, get a new input
                print("Sorry, I don't know what to do with that input.")
                continue  # get new input
                
            if str_guess[0]=='-':
                print("Sorry, positive numbers only. Please try again!")
                continue  # get new input
            elif len(str_guess) != len(secret):
                print("Oops! Your guess should contain "+str(len(secret))+ " digits. Please try again!")
                continue  # get new input

            count += 1  # if it's a valid guess, increment the counter
            list_guess = guess_to_list(str_guess)
            result = guess(list_guess, secret)  # process integer list input
            if result=="Bagels":  # do some 'hint' processing if we get "Bagels"
                for digit in list_guess:
                    if len(hint)==0:
                        hint = [int(digit)]
                    elif digit not in hint:
                        hint.append(int(digit))
                    hint.sort()
            print(result)
            if result=="Fermi Fermi Fermi":
                if count==1:
                    print("You got it on your first guess. Lucky!")
                else:
                    print("You got it after",count,"guesses. Nice job!")
                play_again = True

        if play_again:
            if input("\nPlay again (y/N)? ").lower()=="y":
                play_again = False
                secret = generate_secret()
                hint = []
                count = 0
            else:
                done = True
    print("Okay. Thanks for playing!")  # after the while loop, so exit
    
# if standalone, run the game from here
if __name__ == "__main__":
    bagels()
