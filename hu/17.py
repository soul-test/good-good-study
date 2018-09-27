# enconding: utf-8

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
sum=day  #定义一个变量，承接天数
i = 0  #定义循环次数
days = [31,28,31,30,31,30,31,31,30,31,30,31] #为了简单，定义一个列表存放天数

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)): #判断是否是闰年，是的话，2月天数29天
    days[1] = 29
while i < month-1:   #从0开始循环，循环到输入的前一个月，把所有的天数组合起来，再加上当月的天数。
    sum = sum + days[i]
    i+=1
print('it is the', sum, 'day')
