
import random
number = ''.join(random.sample("0123456789", 3))
print(number)
split_num = [int(char) for char in str(number)]
print(split_num)

num1 = split_num[0]
num2 = split_num[1]
num3 = split_num[2]

# print("lookie here!")
# print(num1, num2, num3)

theenum=(num1*100+num2*10+num3)
userguess = 0
# create answer array
answerarray = []


while theenum != userguess:
    x, y, z = input("Pick 3 non-repeating numbers")
    x = int(x)
    y = int(y)
    z = int(z)
    userguess = (a*100+b*10+c)
print(theenum)

userguess = int(input("Pick a number!"))

if theenum == userguess:
    print("You've got it!")
else:
    print("Wrong!")









# Random number generation

# from random import randint
# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
# print(random_with_N_digits(3))
#
# import random
# number = ''.join(random.sample("0123456789", 3))
# print(number)
#
# num = random.randint (0,999)
# print (num)

# from random import shuffle
# l = [i for i in range(10)]
# shuffle(l)
# n = l[0] + 10 * (l[1] + 10 * (l[2] + 10 * l[3]))

# import random
#
# num = []
# num = [0,1,2,3,4,5,6,7,8,9]
# x = random.shuffle(num)
# y = random.shuffle(num)
# z = random.shuffle(num)
