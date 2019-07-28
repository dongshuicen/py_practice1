from unittest import TestCase

from practice.People import Student


class StudentTest(TestCase):
    def test_study(self):
        stu = Student('Test_ZhangSan', 40, 60, 'Luo Yang Tech 2008 TC')
        self.assertEqual('Test_ZhangSan 学号 Luo Yang Tech 2008 TC 正在学习', stu.study())