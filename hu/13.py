#encoding: utf-8
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的"三位数"？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。只要在各个位置位数循环就可以，要注意不能重复，所以要除去相同的情况

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and ( i != j ) and ( j != k ):
                print(i,j,k)
