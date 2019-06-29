# -*- coding: utf-8 -*-
while True:
    name = input('请输入姓名：')
    if name != 'a':
        print(name)
        # name = input('姓名不正确，请重新输入：')
        print('姓名不正确，请重新输入：')
    else:
        print('欢迎：{0}'.format(name))
        break