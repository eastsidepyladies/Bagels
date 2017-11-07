import random

def pick_num():
	num = []
	for int in range(0,10):
		num.append(int)
		
	#print(num)
	
	random.shuffle(num)
	
	#print(num)
	
	return num[0:3]
	
print(pick_num())