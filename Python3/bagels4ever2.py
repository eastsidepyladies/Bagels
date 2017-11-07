playagain=('y')
while playagain == 'y':
    import random
    bagels=0
    number=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number)
    print("Welcome to the Game of Bagels!")
    print("Your goal is to guess my 3-digit number")
    print("None of my numbers will repeat")
    print("I will give you clues:")
    print("Bagels - None of the numbers are correct")
    print("Pico - 1 number is correct, but in the wrong place")
    print("Fermi - 1 number is correct, and in the correct position")
    print(" ")
    #print (number)
    num1=number[0]
    num2=number[1]
    num3=number[2]
    #print (num1,num2,num3)
    totnum=(num1*100+num2*10+num3)
    userguess=0
    answerarray=[]
    while totnum != userguess:
        a, b, c=input('Please input your unique three-digit number :    ')
        a=int(a)
        b=int(b)
        c=int(c)
        userguess=(a*100+b*10+c)
        if totnum == userguess:
            print("You win!!")
            print(' ')
            break
        if num1 == a:
            answerarray.append('Fermi ')
        elif num1 == b or num1 == c:
            answerarray.append('Pico ')
        else:
            bagels=bagels+1
        if num2 == b:
            answerarray.append('Fermi ')
        elif num2 == a or num2 == c:
            answerarray.append('Pico ')
        else:
            bagels=bagels+1
        if num3 == c:
            answerarray.append('Fermi ')
        elif num3 == a or num3 == b:
            answerarray.append('Pico ')
        else:
            bagels=bagels+1
        if bagels == 3:
            print('bagels')
        bagels=0
        random.shuffle(answerarray)
        print(*answerarray) #takes the [''] from answer string
        print(" ")
        answerarray=[]
    playagain=input("Would you like to play again? (y or n)")
    print(' ')
    if playagain == 'n':
        break
        
    
    





