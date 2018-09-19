import random
shu = random.randint(0,100)

count = 1

while count <=5:
    guess = int(input('请输入一个数字: '))
    if guess == shu:
        print('猜对了')
        break
    elif guess < shu:
        print('数字小了')
    else:
        print('数字大了')
    count += 1
    if count == 6:
        print('没猜对')
