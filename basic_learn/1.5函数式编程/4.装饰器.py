#如果我们想要在调用一个函数的前后,自动触发其他行为,就需要"装饰器"了
#这类似于PHP中的构造函数与析构函数

#假设now函数可以输出当前的系统时间,我们需要在调用now函数的前后,自动输出Hello World

def now():
    return  '2016-05-20'
print(now())

def log(funcName):
    def wrap():
        print('Hello World 1')
        print(funcName(),funcName.__name__)
        print('Hello World 2')
    return wrap
now=log(now)
now()


