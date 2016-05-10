from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


def getLinks(startLink):
    # 根据六度分隔理论,我们需要从Kevin_Bacon维基页面中词条的链接访问到Eric_Idle的页面
    html = urlopen("https://en.wikipedia.org" + startLink)
    bsobj = BeautifulSoup(html, 'html.parser')

    # 通过分析,我们发现词条链接相比较于侧边栏,页眉,页脚链接,具有如下特点
    # 1.都在id为bodyContent的元素里面
    # 2.以/wiki/开头
    # 3.不包含冒号
    return bsobj.find(id='bodyContent').findAll('a', {'href': re.compile('^/wiki/[^:]*$')})


links = getLinks('/wiki/Kevin_Bacon')

while (len(links) > 0):
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
