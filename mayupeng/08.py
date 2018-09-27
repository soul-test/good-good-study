users = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))


'''
format:name.age,tel
编号--> 要的当前最大的ID+1
split --> ,
'''

while True:
    data = input('请输入新需要创建的用户信息(name,age,tel)：')
    txt = data.split(',')

    if len(txt) != 3:
        print('格式错误，是不是傻')
    else:
        for user in users:
            uid = 0
            if user[0] > uid:
                uid = user[0]

        txt[1] = int(txt[1])
        users.append(((uid + 1,) + tuple(txt)))
        print(users)

