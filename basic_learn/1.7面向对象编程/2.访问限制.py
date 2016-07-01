# 私有属性的声明就是在命名前加上 __,例如__abc

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        return '姓名是%s,分数是%s' % (self.__name, self.__score)


stu = Student('zqq', 12)
print(stu.print_score())
# 报错,提示无此属性
# print(stu.__name)
# print(stu.__score)
