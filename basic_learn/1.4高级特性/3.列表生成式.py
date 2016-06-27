import os

# 生成从0到20的列表
print(list(range(0, 20)))
# 生成从0到20的平方的列表
print(list(x * x for x in range(0, 20)))
# 生成从0到20的偶数的平方的列表
print(list(x * x for x in range(0, 20) if x % 2 == 0))

# 生成配对列表
print(list(x + y for x in ('ABC') for y in ('XYZ')))

# 生成当前目录下的文件列表
print(list(d for d in os.listdir('.')))

# 将列表转换为小写
print(list(str.lower() for str in ['Zqq', 'Yfx']))

# 将既含有数字,又含有字符串的list转换为小写,进行容错处理
print(list(x.lower() for x in [1, 2, 'A', 3, 4, 'B', 'c'] if isinstance(x, str)))
