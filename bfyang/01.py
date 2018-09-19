import random
shu = random.randint(0,100)

count = 1

while count <= 5:
    cai = int(input('请输入一个数字: '))
    if cai == shu:
        print('猜对了!')
        break
    elif cai < shu:
        print('猜小了')
    else:
        print('猜大了')
    count += 1
    if count == 6:
        print('很遗憾,再来一次')
