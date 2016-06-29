# 返回函数意味着返回的将不是一个具体的数值,而是一个函数

def func(*args):
    def func_internal():
        total = 0
        for x in args:
            total += x
        return total

    return func_internal


result = func(1, 2, 3, 4)
print(result)
print(result())

# 需要注意的是,即使传入的是相同的参数,两次返回的函数也是不同的
print(func(1, 2, 3, 4) == func(1, 2, 3, 4))

# 闭包,暂不执行
def func(*args):
    result = []
    for num in args:
        def func_internal():
            return num*num
        result.append(func_internal)
    return result
result=func(1,2,3,4)
print(result[0]())  #16
print(result[1]())  #16
print(result[2]())  #16
print(result[3]())  #16

#闭包,及时执行
def func(*args):
    result = []
    for i in args:
        def func_internal(j):
            def func_internal_internal():
                return j*j
            return func_internal_internal
        result.append(func_internal(i))
    return result
result=func(1,2,3,4)
print(result[0]())  #16
print(result[1]())  #16
print(result[2]())  #16
print(result[3]())  #6


