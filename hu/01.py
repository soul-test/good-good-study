a = input("猜猜哥是几月的：")
b = int(a)
while b != 8:
   a = input("在给你次机会吧：")
   b = int(a)
   if b == 8:
       print("猜对又如何？")
       print("在bb我打你！")
   else:
        if b > 8:
            print("你可以往前考虑考虑")
        else:
            print("往小点猜好不好?")
print("GG! 不玩咯！")
