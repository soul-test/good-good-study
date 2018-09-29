num = []
while True:
	promit = input('请输入一个任务或者do:')
	if  promit != 'do':
	    num.append(promit)
	else:
		if len(num) > 0:
			print(num.pop(0))
		else:
			break

