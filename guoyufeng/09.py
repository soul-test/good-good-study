a='|{0:^10s}|{1:^10s}|{2:^10s}|{3:^20s}|'
b=('totle','name','age','add')
c=a.format(b[0],b[1],b[2],b[3])
i=1
name=0
d=[]
while name != 'q':
   name=input('name:')
   if name == 'q' :
       break
   age=str(input('age:'))
   add=str(input('add:'))
   d.append(a.format(str(i),name,age,add))
   i=i+1
print('-'*len(c))
print(c)
print('-'*len(c))
for e in range(0,i-1):
   print(d[e])
