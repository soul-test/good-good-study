import random
simple = random.randint(0,50)

count = 1

while   count <= 5:
    guess = int(input('请输入一个数字： '))
    if guess == simple:
        print('你真牛！')
        break
    elif guess < simple:
        print('你说那数小勒！')
    else:
        print('你说那数大勒！')
    count += 1
    if count == 6:
        print('大笨蛋，重猜!')