from collections import Iterable

# 列表生成式用于生成一个数组
print([x * x for x in range(0, 20) if x % 4 == 0])

# 生成器用于保存一个算法
# ===============================================定义生成器的第一种方法===================================
# 将列表生成式的[]符号改写为()符号
g = (x * x for x in range(0, 20) if x % 4 == 0)
print(g)

# 使用next函数可以获取生成器下一次返回来的值
print(next(g))  # 0
print(next(g))  # 16
print(next(g))  # 64
print(next(g))  # 144
print(next(g))  # 256
# print(next(g))  # 无返回值时,会报StopIteration错误

# 迭代生成器返回的值
print(isinstance(g, Iterable))  # True,说明此类型可以迭代

g = (x * x for x in range(0, 20) if x % 4 == 0)
for v in g:
    print(v)


# ===============================================定义生成器的第二种方法===================================
# 在函数中使用yield
def add():
    print(1)
    yield
    print(2)
    yield
    print(3)
    yield


g = add()  # 包含yield关键字的函数必须先赋给一个变量才可以使用next()来调用
print(add())  # 包含了yield关键字的函数就是生成器了
next(g)  # 1
next(g)  # 2
next(g)  # 3


# 从以上结果中我们可以看出生成器在执行的过程中,遇到yield关键字就会终止执行,而下一次的执行又会在上一次的基础上进行

# 正常情况下,我们是无法获取含有yield关键字的函数的返回值的,因为此时的返回值为StopIteration的value
def increase():
    return 100
    yield
    return 101
    yield
    return 102
    yield


g = increase()
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e.value)
        break
