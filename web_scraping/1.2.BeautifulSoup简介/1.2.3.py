from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 容错处理,定义一个获取页面title的getTitle函数
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        # 如果服务器返回404,500等错误
        return None
    else:
        # 成功打开页面
        print("Hello World")
    try:
        bsobj = BeautifulSoup(html.read(), "html.parser")
        title = bsobj.title
    except AttributeError  as e:
        return None
    return title
title = getTitle('http://www.siguoya.name/')
if title is None:
    print('节点不存在')
else:
    print(title)
