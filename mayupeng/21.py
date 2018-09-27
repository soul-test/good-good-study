a = int(input('查询成绩:'))
x = 9 - a // 10
if x == -1: 
    x =0
if x >4:
	x = 4
print('你们的成绩是:' + chr(ord('A') + x))

