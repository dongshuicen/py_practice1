# 类定义
import datetime
from distutils.log import Log

from practice.If_Test import getType


class People:
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁, 体重 %d 斤。" % (self.name, self.age, self.__weight))

    def justPeopleType(self):
        print(getType(10).isdigit())
        return getType(self.age)


# 实例化类
print(datetime.date.today())
print(datetime.datetime.today())
print(datetime.date(2019, 7, 20))
p = People('runoob', 10, 30)
p.speak()


class Student(People):
    studentNo = None

    def __init__(self, name: str, age: int, weight: int, student_no: str):
        super(Student, self).__init__(name, age, weight)
        self.studentNo = student_no

    def study(self):
        message = "%s 学号 %s 正在学习" % (self.name, self.studentNo)
        print(message)
        return message


stu = Student('张三', 18, 50, '20190817')
stu.speak()
stu.study()
Log.info(Log, 'People end', None)