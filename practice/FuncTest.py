# -*- coding:utf-8 -*-
def variableTest(name = "not name", age = 0):
    global gname
    name = 'func1'
    gname = 'variableTest in process'
    age = 2
    print(name)
    print(age)

name = 'dsc'
age = 18
gname = 'init start'
variableTest(age, name)
print(name)
print(age)
variableTest()
print(gname)