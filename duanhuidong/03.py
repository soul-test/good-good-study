b = []

while True:
    a = input('请输入一个任务或do：')
    if a != 'do':
       b.append(a)
    else:
       if b:
        print(b.pop(0))
       else:
        print('放假了')
        break

