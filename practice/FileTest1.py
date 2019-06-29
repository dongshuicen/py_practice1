# -*- coding: UTF-8 -*-
file1 = open("text2.txt", "a+")
file1.write("hello python ;\n very good \n")
file1.close()
# read file
try:
    file1 = open("text2.txt", "r")
except(IOError):
    print("文件没有找到!")
else:
    str = file1.read(100)
    print("文件text2.txt内容是："+str)