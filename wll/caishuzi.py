import random
sj = random.randint(1,100)

count = 1
while count <= 5 :
    guess = int(input('number: '))
    if guess == sj:
        print('你真棒')
        break
    elif guess < sj:
        print('猜小了')
    else :
        print('猜大了')
    count += 1
    if count ==6:
        print('太笨了，重来')

