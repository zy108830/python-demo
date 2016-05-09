from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.siguoya.name/')
bsobj = BeautifulSoup(html.read(), 'html.parser')

# BeautifulSoup可以直接以对象的形式获取页面的节点,厉害凸^-^凸
print(bsobj.title)
print(bsobj.script)
