num=[]
while True:
  a=input('qingshuru:')
  if a == 'do':
     if num:
        print(num.pop(0))
     else:
        break
  else:
       num.append(a)
      
