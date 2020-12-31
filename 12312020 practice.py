#12312020 practice

import random
""" r = random.randint (1, 100)
count = 0
while True :
    num = input ('please pick a number : ')
    num = int (num)
    count += 1 #==>就是count = count + 1 的意思，這個只是純粹的快寫
    if num == r :
        print('Bingo!')
        print('You have tried', count , 'times to acheive!')
        break
    elif num > r :
        print('Too large! Try a smaller one!')
    elif num < r :
        print ('Too small! Try a larger one!')
    print ('You have tried', count , 'times')
 """


range_start = input ('please choose the range you want to start: ')
range_end = input ('please choose the range you want to end: ')
range_start = int(range_start)
range_end = int(range_end)
r = random.randint (range_start, range_end)
count = 0
while True :
    num = input ('please pick a number : ')
    num = int (num)
    count += 1 
    if num == r :
        print ('Bingo!')
        print ('You have tried', count , 'times to acheve!')
        break
    elif num > r :
        print ('Too large! Try a smaller one')

    elif num < r :
        print ('Too small , Try a larger one')
    print ('You have tried', count , 'times so far!')
