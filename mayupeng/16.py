users = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))



update_user = None     #变量的初始化

uid = int(input('请输入要修改用户的ID：'))  #让用户输入修改的ID
for user in users:
    if uid == user[0]:       #判断ID在不在系统中
        update_user = user    #在的话就把这个元组信息给update_user变量
        break                     #退出
    else:
        print('用户不存在')    #不在就打印
if update_user:     #如果存在，就是真，执行下面
    data = input('请输入新创建的用户信息(name,age,tel)：')
    txt = data.split(',')
    if len(txt) != 3:
        print('格式错误，是不是傻')                             #这边和增加一样
    else:
        users.remove(update_user)                            #因为修改，uid不变，所以删除最大uid语句，并且要先删除找到的原信息
        txt[1] = int(txt[1])                            
        users.append(((uid,) + tuple(txt)))                   #重新添加，注意uid不变
        print(users)                   #测试sers = []
users.append((0,'soul',18,'132xxxxxx'))
users.append((1,'test',21,'138xxxxxx'))
users.append((2,'gg',8,'134xxxxxx'))

update_user = None

uid = int(input('请输入要修改用户的ID：'))  #判断ID在不在系统中
for user in users:
    if uid == user[0]:
        update_user = user
        break
    else:
        print('用户不存在')
if update_user:
    data = input('请输入新创建的用户信息(name,age,tel)：')
    txt = data.split(',')
    if len(txt) != 3:
        print('格式错误，是不是傻')
    else:
        users.remove(update_user)
        txt[1] = int(txt[1])
        users.append(((uid,) + tuple(txt)))
        print(users)
