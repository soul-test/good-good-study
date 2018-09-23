users = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))


while True:
    data = int(input('请输入要删除的用户ID：'))
    for user in users:
        if data == user[0]:
            users.remove(user)
            print(users)
            break
        else:
            print('ID不存在')
