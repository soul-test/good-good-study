import random
sj = random.randint(0,100)

count = 1
while count <=5:
    guess = int(input('请输入一个数字：'))
    if guess == sj:
        print('厉害厉害！')
        break
    elif guess < sj:
        print('猜小了，笨死了！')
    else:
        print('哎呀又猜大了！')
    count += 1
    if count == 6:
        print ('简直了，太笨!')
    
