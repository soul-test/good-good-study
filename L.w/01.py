import random
sj = random.randint(0,100)

count = 1

while   count <=5:
    guess = int(input('xie shu zi: '))
    if guess == sj:
         print('zhen bang!')
         break
    elif guess < sj:
         print('tai xiao!')
    else:
         print('tai da!')
    count += 1
    if count ==6:
       print('tai sha!')

