# 它查找Python的request模块,但是只导入一个urlopen函数
from urllib.request import urlopen
html = urlopen("http://www.siguoya.name/")
print(html.read())
