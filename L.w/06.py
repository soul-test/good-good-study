users = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))

'''
----------------------
 10s 10s 5s   15s
|ID|姓名|年龄|联系方式|
----------------------
 10d 10s   5d    15s
|0|'soul'|18|'132xxxxxx'|
|1|'soul2'|16|'134xxxxxx'|
-----------------------
'''

while True:
    select = input('请选择你的操作(add/list/delete/update/find/exit):')
    if select == 'add':
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
    elif select == 'list':
        a_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
        b_title = ('ID','name','age','tel')
        title = a_title.format(b_title[0],b_title[1],b_title[2],b_title[3])
        line = '-' * len(title)

        data_format = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'

        print(line)
        print(title)
        print(line)

        for user in users:
            print(data_format.format(user[0],user[1],user[2],user[3]))
        print(line)
    elif select =='find':
        data = input('请输入需要查找的用户名：')
        for user in users:
            if user[1] == data:
                print(line)
                print(title)
                print(line)
                print(data_format.format(user[0],user[1],user[2],user[3]))
                print(line)
    elif select == 'delete':
        data = int(input('请输入要删除的用户ID：'))
        for user in users:
            if data == user[0]:
                users.remove(user)
                break
            else:
                print('ID不存在')
                break
    elif select == 'update':
        update_user = None     #变量的初始化
        uid = int(input('请输入要修改用户的ID：'))  #让用户输入修改的ID
        for user in users:
            if uid == user[0]:       #判断ID在不在系统中
                update_user = user    #在的话就把这个元组信息给update_user变量
        if update_user:     #如果存在，就是真，执行下面
            data = input('请输入新创建的用户信息(name,age,tel)：')
            txt = data.split(',')
            if len(txt) != 3:
                print('格式错误，是不是傻')                             #这边和增加一样
            else:
                users.remove(update_user)                            #因为修改，uid不变，所以删除最大uid语句，并且要先删除找到的原信息
                txt[1] = int(txt[1])                            
                users.append(((uid,) + tuple(txt)))                   #重新添加，注意uid不变
        else:
            print('用户不存在')
            exit()
    else:
        exit()
