# 声明一个学生类,然后对其实例化
# Student(object)表示这个类继承于object
# 类的方法与普通函数的区别就是,类的方法的第一个参数永远都是实例变量self
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        return '姓名是%s,分数是%s' % (self.name,self.score)

stu=Student('zqq',12)
print(stu.name)
print(stu.score)
print(stu.print_score())