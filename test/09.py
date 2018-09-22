users = []

users.append((1,'kk',29,'136xxxxxxx'))
users.append((2,'qq',15,'126xxxxxxx'))
users.append((3,'aa',2,'134xxxxxxx'))
users.append((4,'zz',14,'131xxxxxxx'))

'''
-----------
10s  10s 5s    15s
|ID|姓名|年龄|联系方式|
|1|kk|12|13445|
----------------
'''

tpl_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
columes_title = ('ID','Name','Age','Tel')

title = tpl_title.format(columes_title[0],columes_title[1],columes_title[2],columes_title[3])

splitline= '-' * len(title)
tpl_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'
splitline= '-' * len(title)

print(splitline)
print(title)
print(splitline)

for user in users:
    print(tpl_body.format(user[0],user[1],user[2],user[3]))
print(splitline)

