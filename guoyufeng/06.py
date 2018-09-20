a=[1,2,5,4,10,20,3]
for x in range(len(a)-1):
   for i in range(len(a)-x-1):
      if a[i] > a[i+1]:
           b=a[i]
           a[i]=a[i+1]
           a[i+1]=b
print(a)
