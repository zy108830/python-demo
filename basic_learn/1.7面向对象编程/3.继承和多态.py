# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return '我的名字是%s,我的年龄是%d' % (self.name, self.age)


# 实现继承
class Student(Person):
    pass


stu = Student('zqq', 24)
print(stu.intro())
