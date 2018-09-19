import random 
sj = random.randint(0,100)

count = 1

while count <= 5:
    guess = int(input('请输入一个数字：'))
    if guess == sj:
        print('恭喜你，答对了！')
        break
    elif  guess < sj:
        print('数字猜小了！')
    else :
        print('数字猜大了！')
    count += 1
    if count == 6:
        print('太笨了，游戏结束，投币再来一次！')
