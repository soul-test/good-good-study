import random
sj = random.randint(0,100)
count = 1
while   count <= 5:
    guess = int(input('请输入一个数字:'))
    if guess == sj:
        print('你真棒:')
        break
    elif guess < sj:
        print('数字猜小了:')
    else:
        print('s数字猜大了:')
    count += 1
    if count == 6:
        print('太笨了,请重新投币!')

