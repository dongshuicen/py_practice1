# -*- coding: UTF-8 -*-
def hello(name, age):
    print("name:" + name)
    print("age:" + str(age))
    return


hello("dongshuicen", 30)

array = [1,2,3,4,5,6,7,8]
print(array[0])
array[1]=10
print(array[1])
#yuanzu=[]
lambdatest='lambdatest'
lambdatest='bbc'
print(lambdatest)
tup1 = (1,2,3,4,5,6)
#tup1[0] = 2
print(tup1[1])
dict1={"1" : 1,"2" : 2, "3" : 3}
print(dict1["1"])
print(dict1["3"])
dict1["1"] = "更新值!"
print("字典更新后值："+str(dict1["1"]))
str = input("请输入：")
print(str)
#if __name__ == '__main__':
#    hello("dong", 30)
#from mailbox import *
print('符号'+'\'')