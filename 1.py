import random
sj = random.randint(0,100)
count = 1
while count <= 5:
   guess =int(input('请输入一个数字: '))
   if guess == sj:
      print('真棒，答对了! ')
      break
   elif guess < sj:
      print('数字猜小了! ')
   else :
      print('数字猜大了! ')
   if count == 6:
      print('太笨了,再来一次! ')
