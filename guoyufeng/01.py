a=1
while a < 10 :
  b=1
  while b <= a:
     print(b , '*' , a , '=' , b * a ,' ',end="")
     if b == a:
       print('\n')
     b = b + 1
  a= a + 1

