from collections import Iterable
#判断一种数据类型能否被迭代
print(isinstance((1,2,4) ,Iterable))
# 迭代dict类型
names = {'zqq': 22, 'yfx': 21}
for k, v in names.items():
    print(k, v)

# 迭代list类型的元素
names = ['zqq', 'yfx']
for name in names:
    print(name)

# 迭代list类型,以key-value的形式
names = ['zqq', 'yfx']
for index, name in enumerate(names):
    print(index, name)


