lie = []

while True:
   t = input('请输入任务或者do: ')
   if t != 'do':
      lie.append(t)
   else:
       if len(lie) > 0:
           print(lie.pop(0))
       else:
           print('下课了！')
           break

