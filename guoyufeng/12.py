a=[1,2,3,4]
b=[]
j=0
for i in a:
   for d in a: 
     for c in a:
       if i != d and i !=c and d != c :
          print(i*100+d*10+c)
          j=j+1
print(j) 
