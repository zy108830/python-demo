# 它查找Python的request模块,但是只导入一个urlopen函数
from urllib.request import urlopen
for x in range(10):
    try:
        html = urlopen("http://www.siguoya.name/" + str(x))
    except BaseException:
        print(x)
