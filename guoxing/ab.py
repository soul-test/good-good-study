num = []
while True:
    shuru  = input('输入do或者非do:')
    if shuru != 'do':
        num.append(shuru)
    else:
        if num:
            print(num.pop(0))
        else:
            break
