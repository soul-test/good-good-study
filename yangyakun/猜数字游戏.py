import random
sj = random.randint(0,100)

count = 1

while count <= 5:
	guess = int(input('请您先输入一个数字: '))
	if guess == sj:
		print('你真棒！')
		break
	elif guess < sj:
		print('数字有点小！')
	else:
		print('数字有点大！')
	count = count + 1
	if count == 6:
		print('对不起，您的智商有限，不适合此类游戏')