import random

def play_game():
	print("\nWelcome to Bagels")
	print("I will pick a 3 digit number with 3 unique digits.")
	print("Guess a 3 digit number and I'll tell you if any of the digits are correct.\n")
	print("I'll say Bagels or B, if none of the digits you guess are in my number.\n")
	print("If a digit is in my number, but in the wrong place, I'll say Pico or P.\n")
	print("If a digit is in the same place as my number, I'll say Fermi or F.\n")
	print("Guess a number to begin")
	mystery_num = pick_num()
	correct = False
	while not correct:
		#Ask player to guess
		#print result
		#if FFF set correct to True
		correct = True
	


def pick_num():
	num = []
	for int in range(0,10):
		num.append(int)
		
	#print(num)
	
	random.shuffle(num)
	
	#print(num)
	
	return num[0:3]
	
#print(pick_num())

play_game()

