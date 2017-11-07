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

import random
num = [0,1,2,3,4,5,6,7,8,9]
x = random.shuffle(num)
y = random.shuffle(num)
