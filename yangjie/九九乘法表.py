num = 1

while num <= 9:
	i = 1
	while i <= num:
		print(str(i) + '*' + str(num) + '=' + str(i*num), end="\t")
		i += 1
	print()
	num += 1
