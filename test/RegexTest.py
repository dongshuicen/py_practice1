# -*- coding:utf-8 -*-
import re
while True:
    val = input('请输入您的年龄：')
    if val.isdigit():
        if int(val) < 0:
            print('请输入大于0的年龄！')
        else:
            print('您输入的年龄是：' + val)
            break
    else:
        print('请输入数字')
val = input('请输入：')
digit = re.compile(r'\d')
mo = digit.search(val)
try:
    print(mo.group())
except:
    print('报错了')
