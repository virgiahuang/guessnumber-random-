#122920 python practice

""" import random
r = random.randint(1,10)
while True:
    num = input('Please enter a random number (1-10):')
    num = int(num)
    if num == r :
        print ('Bingo!')
        break
    elif num > r :
        print ('too large')
    elif num < r :
        print ('too small') """


import random
r = random.randint (1,10)

while True :
    num = input ('please pick a number :')
    num = int (num)
    if num == r :
        print ('Bingo!')
        break
    elif num > r :
        print ('Too large!')
    elif num < r :
        print ('Too small!')