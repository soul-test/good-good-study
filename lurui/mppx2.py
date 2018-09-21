num = [1,24,8,3,5,7]
x = 0
y = 0
a = 0

print('要排序的数字为：', str(num))

for y in range(len(num) - 1) :
  for x in range(len(num) - y - 1) :
    if num[x] > num[x+1] :
      a = num[x]
      num[x] = num[x+1]
      num[x+1] = a

print('排序后的数字为：',str(num))
