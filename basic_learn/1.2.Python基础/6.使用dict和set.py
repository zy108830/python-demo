# =====================================================dict========================================
# dict可以理解为js中的对象
d = {
    'name': 'zqq',
    'age': 22
}
print(d)
print(d['age'])

# 如果指定的key不存在,那么在取出的时候就会报错,这个时候就需要容错处理
# 判断key是否存在
print('sex' in d)
# dict的get方法还可以给出一个默认值
print(d.get('sex', '男'))

# 输出可以迭代的dict值集合
print('values:',d.values())
print('items:',d.items())

# 迭代d的key
for key in d:
    print('key:', key, 'value:', d[key])
#迭代d的key=>value
for k,v in d.items():
    print(k,v)

# ====================================================set=============================================
# 创建一个set,需要传入一个list类型的变量----->set是无序的,不存在重复元素的list
awardCode = set([1, 2, 3, 3, 3, 10])
print(awardCode)

# 通过add方法可以往set中添加元素,remove方法从set中移除元素
s1 = set([1, 2, 3, 4, 5])
s1.add(6)
# 多次添加无效
s1.add(6)
s1.add(6)
s1.add(6)
print(s1)
s1.remove(1)
# 如果多次移除同一个元素的话,也会报错
print(s1)

# 利用&与||方法,可以实现数学意义上的交并集
s2 = set([1, 2, 3, 4])
s3 = set([3, 4, 5, 6])
print(s2 & s3)  # 交集
print(s2 | s3)  # 并集
