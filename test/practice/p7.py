#encoding: utf-8
#题目：输出 9*9 乘法口诀表。

#程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

m = 1 #定义一个起始量

while m <= 9:
    i = 1
    while i <= m:
        print(str(i) + '*' + str(m) + '=' + str(i*m),end="\t")#end代表不要print的默认输出空格
        i += 1  #i = i + 1
    print()
    m += 1
#
