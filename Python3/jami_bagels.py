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
	print(mystery_num)
	correct = False	
	while not correct:
		#Ask player to guess
		guess = input('Select a number >')
		guess = int(guess)
		while guess < 100 or guess > 999:
			guess = input('Select a 3 digit number >')
			guess = int(guess)
		#print result
		result = player_guess(guess, mystery_num)
		if result == "FFF":
			#if FFF set correct to True
			correct = True
			print('Fermi, Fermi, Fermi!')
			print('Congratulations!, you guessed the correct number of ' + str(guess))
		elif result == "B":
			print('Bagels, Sadly none of those digits are in my number')
		else:
			print(result+ '. So close, you should try again.')
		
	


def pick_num():
	num = []
	for int in range(0,10):
		num.append(str(int))
		
	#print(num)
	
	random.shuffle(num)
	
	#print(num)
	
	return num[0:3]
	
def player_guess(guess, num):
	guess = str(guess)
	pico = 0
	fermi = 0
	for index in range(0, 3):
		if guess[index] == num[index]:
			fermi += 1
		elif guess[index] in num:
			pico += 1

	if pico < 1 and fermi < 1:
		return 'B'
	else:
		result = ""
		for f in range(0, fermi):
			result += 'F'
		for p in range (0, pico):
			result += 'P'
		return result
		
		
	
	
#print(pick_num())

play_game()

