# 获取字符串长度
helloStr = 'Hello World'
print(len(helloStr))

# 使用%号,再通过指定格式对字符串进行格式化
helloStr = 'siguoya : %d , Male : %s' % (22, True)
print(helloStr)

# 字符串替换
name = 'zqq'
print(name.replace('z', 'y'))

# 字符串截取
name = 'zqq'
print(name[:1])
print(name[-2:])

# 字符串拼接
print('A' + 'B')
print('A', 'B')

# 字符串大小写转换
print('A'.lower())

# 字符串去空格，详见 http://www.jb51.net/article/33631.htm
print(str.strip('  A  '))
