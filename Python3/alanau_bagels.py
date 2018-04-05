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
def guess(str_guess, secret):
    fermi = pico = 0
    output = []

    try:
        int_guess=int(str_guess)
    except ValueError: # if not an integer, get a new input
        return("Sorry, I don't know what to do with that input.")
        
    if str_guess[0]=='-':
        return("Sorry, positive numbers only. Please guess again!")
    elif len(str_guess) != len(secret):
        return("Oops! Your guess should contain "+str(len(secret))+ " digits. Please try again!")

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

# if Bagels, call this to update hint[] to track bad guesses
def update_hint(list_guess,hint):
    for digit in list_guess:
        if len(hint)==0:
            hint = [int(digit)]
        elif digit not in hint:
            hint.append(int(digit))
        hint.sort()
    return(hint)
    
def give_hint(hint):
    if len(hint) > 0:
        print("You know that the answer doesn't contain these numbers:", " ".join(list(map(str,hint))))
    else:
        print("Sorry, you haven't learned enough about the numbers in the answer. Try making more guesses!")

def give_answer(secret):
    return ("The answer is "+"".join(list(map(str,secret))))

def greeting():
    greet_text = "Welcome to Bagels! Say Help for instructions, or start playing by guessing 3 digits."
    return(greet_text)

def help():
    help_text = """Welcome to bagels. I have picked a 3-digit non-repeating number.
When you guess three digits, I will say Fermi if a correct digit is in the right place.
I will say Pico is a correcct digit is in teh wrong place.
I will say Bagels if none of the digits is correct.
You can also ask for a hint, ask the answer right away, or to stop playing."""
    return (help_text)
    
# Here's a wrapper to run the game:
def bagels():
    secret = generate_secret()
    done = play_again = False
    hint = []
    count = 0
    
    while not done:
        print(flush=True)
        str_guess = input("Please guess a number: ").lower()
        if str_guess=="answer":
            print(give_answer(secret))
            play_again = True
        elif str_guess=="quit" or str_guess=="exit":
            done = True
            continue  # exit immediately
        elif str_guess=="hint":
            print(give_hint(hint));
        elif str_guess=="help":
            print(help_text)
        else:
            list_guess = guess_to_list(str_guess)
            result = guess(list_guess, secret)  # process integer list input
            hint = update_hint(list_guess, hint)
            count += 1  # if it's a valid guess, increment the counter #FIX ME
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
