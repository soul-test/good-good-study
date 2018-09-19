import random
sj = random.randint(0,100)

count = 1

while count <= 5:
	guess = int(input('Please input a number: '))
	if guess == sj:
		print('You are good!')
		break
	elif guess < sj:
		print('The number is smaller than right answer!')
	else:
		print('The number is bigger than right answer!')
	count += 1
	if count == 6:
		print('sorry,your IQ is limited,it is not suitable for this kind of game,thank you for your participation')
