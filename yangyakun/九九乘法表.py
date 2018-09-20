x = 1

while x <= 9:
	z = 1
	while z <= x:
		print(str(z) + '*' + str(x) + '=' + str(z*x), end="\t")
		z += 1
	print()
	x += 1
