num = [22,35,1,45,26,6,7]
a = 0
x = 0
y = 0

for y in range(len(num)-1):
    for x in range(len(num)-y-1):
        if num[x] > num[x+1]:
            a = num[x]
            num[x] = num[x + 1]
            num[x + 1] = a
print(num)
