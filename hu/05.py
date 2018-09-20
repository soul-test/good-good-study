a=[11,12,323,24,65]
for x in range(len(a)-1):
   for i in range(len(a)-x-1):
    if a[i] > a[i+1]:
      b=a[i]
      a[i]=a[i+1]
      a[i+1]=b
print(a)
