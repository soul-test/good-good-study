users = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))

data = input('请输入需要查找的用户名：')
for user in users:
    if data == user[1]:
        print(user)
'''
不解释，能看懂不
'''
