# 遍历list类型
classmates = ['zqq', 'yfx', True, 1234]
for classmate in classmates:
    print(classmate)

# 遍历tuple类型
classmates = ('a', 'b', 'c', 'd')
for classmate in classmates:
    print(classmate)

# 如果要计算0-100的数值之和,我们手动写[1,2,3,4,5....98,99,100]就比较麻烦

# 方法1, 利用range()函数
# 注意list是前闭后开的区间,range(0,101)等于range(101)
print(range(10))
print(list(range(0, 101)))
print(range(101))
sum = 0
for num in range(101):
    sum += num
print(sum)

# 方法2, 利用while表达式
start = 0
end = 100
sum = 0
while start <= 100:
    sum += start
    start += 1
print('===============================================')
print(sum)
