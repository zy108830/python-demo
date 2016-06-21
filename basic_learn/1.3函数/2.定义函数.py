# 定义一个函数
def abs_alias(num):
    # 容错处理
    if not isinstance(num, (int, float)):
        raise TypeError('错误的参数类型')
    if num <= 0:
        return -num
    else:
        return num


print(abs_alias(-300))


# print(abs_alias('zqq'))


# 定义一个函数,返回多个结果
# 从结果中我们可以看出,返回的多个参数实质上就是一个tuple类型的变量
def return_multi():
    return 1, 2


print(return_multi())

print(aaa(333))
