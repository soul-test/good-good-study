str_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
custom_title = ('ID','姓名','年龄','联系方式')

title = str_title.format(custom_title[0],custom_title[1],custom_title[2],custom_title[3])

print('-' * len(title))
print(title)
print('-' * len(title))
