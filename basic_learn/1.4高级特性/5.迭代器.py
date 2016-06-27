from collections import Iterable
from collections import Iterator
# 能够被for迭代的数据类型有两种
# 一种是集合数据类型,例如list,tuple,dict,set,str等
# 另一种就是生成器了

# Iterable与Iterator的区别在于:
# 我们可以使用isinstance(x,Iterable)来判断一个数据类型能否被迭代
# 我们可以使用isinstance(x,Iterator)来判断一个数据类型能否使用for来迭代,以及使用next来获取下一个返回值
# 集合数据类型以及生成器都是Iterable对象,但只有生成器才是Iterator对象

# 我们可以使用iter函数将Iterable对象转换为Iterator对象

g=[1,2,3]
r=iter(g)
print(isinstance(g,Iterable))
print(isinstance(g,Iterator))

print(isinstance(r,Iterable))
print(isinstance(r,Iterator))

print(next(r))
print(next(r))
print(next(r))

