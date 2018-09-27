#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1,5):
  for j in range(1,5):
    for k in range(1,5):
      if ( i != j ) and  ( i != k ) and ( j != k ): 
        print( i , j , k )

