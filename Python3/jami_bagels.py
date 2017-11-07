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
	# print(mystery_num)
	correct = False	
	while not correct:
		#Ask player to guess
		player_guess = verify_valid_response()
		#print result
		result = check_guess(player_guess, mystery_num)
		if result == "F F F ":
			#if FFF set correct to True
			correct = True
			print('Fermi, Fermi, Fermi!')
			print('Congratulations!, you guessed the correct number of ' + player_guess)
		elif result == "B":
			print('Bagels, Sadly none of those digits are in my number')
		else:
			print(result+ '  So close, you should try again.')
		
	


def pick_num():
	num = []
	for int in range(0,10):
		num.append(str(int))
		
	#print(num)
	
	random.shuffle(num)
	if num[0] == '0':
		return pick_num()
	
	#print(num)
	
	return num[0:3]
	
def verify_valid_response():
	guess = input('Select a number >').strip()
	if guess.isdigit():
		guess = int(guess)
		if guess >= 100 and guess <= 999:
			return str(guess)
	
	return verify_valid_response()
	
def check_guess(guess, num):
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
			result += 'F '
		for p in range (0, pico):
			result += 'P '
		return result
		
		
	
	
#print(pick_num())

# for i in range(1000):
# 	num = pick_num()
# 	if (num[0] == '0'):
# 		print (num)

while True:
	play_game()
	play_again = input('Would you like to play again? Y or N > ')
	if play_again.upper() == 'Y' or play_again.lower() == 'yes':
		pass
		print()
		print()
	else:
		print('Thank you for playing')
		break


