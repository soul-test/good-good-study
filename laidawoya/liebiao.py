
num = []

while True:
    test = input('请输入任务或do：')
    if test != 'do':
        num.append(test)
    else:
        if len(num) > 0:
            print(num.pop(0))
        else:
            print('OK，这些钱都是你了！')
            break