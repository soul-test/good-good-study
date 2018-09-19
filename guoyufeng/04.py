a=[6, 11, 7, 9, 4, 2, 1]
for b in list(range((len(a)-1),0,-1)):
       for c in list(range(0,b)):
           if  a[c] > a[c+1]:
               a[c],a[c+1]=a[c+1],a[c]
print(a)
