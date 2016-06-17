# Python中的if判断语句
s = input('请输入一个数字')
# 用户输入的永远都是字符串,需要先转换为数字,然后再比较
# 如果匹配到了第一个if,那么接下来的都不会再匹配
if int(s) >= 50:
    print('大于50')
elif int(s) >= 10:
    print('大于50')
else:
    print('小于10')