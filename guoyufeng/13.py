a=int(input("totlemoney:"))
b=int(input("lirun:"))
if b <= 10:
   print("zongqianshu" , "=" ,a+b*0.1)
elif   10 <b<=20:
   print("zongqianshu","=",a+10*0.1+(b-10)*0.075)
elif   20 <b<=40:
   print("zongqianshu","=",a+(b-20)*0.05+10*0.1+10*0.075)
elif   40 <b<=60:
   print("zongqianshu","=",a+(b-40)*0.03+20*0.05+10*0.1+10*0.075)
elif   60 <b<=100:
   print("zongqianshu","=",a+40*0.03+20*0.05+10*0.1+10*0.075+(b-60)*0.015) 
elif   b>100:
   print("zongqianshu","=",a+40*0.03+20*0.05+10*0.1+10*0.075+60*0.015+(b-100)*0.001) 
