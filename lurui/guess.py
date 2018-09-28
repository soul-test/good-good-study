'''
猜数游戏
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
'''
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
