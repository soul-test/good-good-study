import random
a = random.randint(0,100)
count = 1
while count <= 5:
     guess = int(input('请输入一个数字: '))
     if guess == a:
        print('你真棒')
        break
     elif guess < a:
        print('数字猜小了')
     else:
        print('数字猜大了')
     count += 1
     if count == 6:
        print('机会用完了，请重新开始') 
