# 高阶函数,就是将一个函数作为参数,去传给另一个函数
def func1(x, y, defName):
    return defName(x, y)


def func2(x, y):
    return x + y


print(func1(1, 2, func2))
