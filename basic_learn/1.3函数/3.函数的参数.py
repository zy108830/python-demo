# ===========================================1.传参类型====================================
# 我们可以像定义PHP函数的默认参数一样,为Python函数定义默认参数
def add(num=1):
    return num + 1


print(add())  # 2


# 但这在默认参数是可变对象的情况下会巨坑,因为默认参数可能会因为之前的调用被修改
def addPlus(L=[]):
    L.append(123)
    return L


print(addPlus())  # [123]
print(addPlus([4, 5, 6]))  # [123,4,5,6]
print(addPlus())  # [123,123]


# ===========================================2.任意多个参数====================================
# 第一种方式,行参不要*号,调用的时候传list类型
def cal(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(cal([1, 2, 3, 4, 5]))


# 第二种方式,行参要*号,正常传参
def cal2(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(cal2(1, 2, 3, 4))


# ===========================================3.关键字参数====================================
def person(name, age, **other):
    return 'name:', name, 'age:', age, 'other:', other


# 只传必填字段的参数
print(person('zqq', 24))
# 传额外的参数,额外的参数要求必须是dict类型
print(person('yfx', 25, **{'lover': 'yfx', 'school': 'gzhu'}))


# ===========================================4.命名关键字参数====================================
# 要求用户名,密码是必填选项,sex与lover是选填选项,其他字段不允许提交
def person2(name, age, *, sex, lover):
    return 'name:', name, 'age:', age, 'sex:', sex, 'lover:', lover


# 传额外的参数,额外的参数必须是sex或lover这些允许的传参
print(person2('zqq', 24, sex='男', lover='yfx'))


# ===========================================5.参数组合====================================
def f1(a, b, *c, **d):
    return 'a:', a, 'b:', b, 'c:', c, 'd:', d


print(f1(1, 2, 3, 4, 5, 6,**{'name':'zqq','sex':'男'} ))
