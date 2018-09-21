'''
提示用户输入do或者任务(非do)
如果用户输入任务，则添加到list中
如果用户输入do，当任务为空时则打印无任务并退出，否则从list中根据先进先出原则打印任务
'''

lst = []
while True:
  do = input('输入do或者任务：')
  if do != 'do':
    lst.append(str(do))
  else:
    if lst:
      print(lst.pop(0))
    else:
      print('done')
      break

