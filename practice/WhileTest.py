# -*- coding:utf-8 -*-
while True:
    age = input('请输入数字：')
    print(type(age).__name__)
    if type(age) != type(int):
        print('类型不正确，请重新输入：')
    else:
        if age < 18:
            print('这是未成年人年龄。。。')
        elif 60 > age >= 18:
            print('这是成年人年龄。。。')
        else:
            print('老年人年龄。。。')
        break