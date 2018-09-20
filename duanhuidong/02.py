a = [4,1,5,2,8]
b = 0

for y in range(len(a)-1):
    for x in range(len(a)-y-1):
        if a[x]>a[x+1]:
           b=a[x]
           a[x]=a[x+1]
           a[x+1]=b
print(a)


