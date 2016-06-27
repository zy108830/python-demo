# =====================================list===================================
# list数据类型即为JS中的数组
classmates = ['zqq', 'yfx']
print(classmates)

# 获取数组元素个数
print(len(classmates))

# 访问第一个数组元素
print(classmates[0])

# 访问倒数第一个数组元素
print(classmates[-1])

# 添加一个元素
classmates.append('our')
print(classmates)

# 插入元素到指定位置
classmates.insert(1, '皮蛋')
print(classmates)

# 删除末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(1)
print(classmates)

# 替换某个位置的元素
classmates[1] = 'congtou'
print(classmates)

# 添加不同类型的元素
classmates.append(True)
print(classmates)

# 在数组中添加数组
classmates.append(['zqq', 'yfx'])
print(classmates)

# 迭代list,enumerate可以将list类型转换为类似dict的键值对类型
names = ['zqq', 'yfx', 'congtou']
for k,v in enumerate(names):
    print(k,v)

# =====================================tuple===================================

# tuple和数组类似,但是tuple在定义的时候,元素必须被确定下来
# 空t
t = ()
print(t)

# 有两个元素的t
t = (1, 2)
print(t)

# 获取tuple元素的方法和list的方法是一样的
print(t[1])

# 只有一个元素的t,后面也必须加逗号,避免混淆数学中的括号
# t是数字
t = (1)
print(t)

# t是tuple类型的数据类型
t = (1,)
print(t)

# tuple本身不可以变,但它的元素可以变
t = (1, 2, ['zqq', 'yfx'])
print(t)
t[2].append('our')
print(t)

# tuple截取
t = (1, 2, 3)
print(t[2:])
print(t[-2:])
