from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

internalLinks = set()


# 获取网站根目录或指定目录下的列表
def getInternalLinks(pageUrl, host, scope):
    print('总链接数量:' + str(len(pages)))
    print('所要访问的页面地址:' + host + pageUrl)
    html = urlopen(host + pageUrl)
    bsobj = BeautifulSoup(html, 'html.parser')
    links = bsobj.findAll('a', {'href': re.compile('^' + scope)})
    print('所访问的页面的链接总数:' + str(len(links)) + '\n===========')
    for link in links:
        if link.attrs['href'] not in pages:
            newArticle = link.attrs['href']
            pages.add(newArticle)
            getInternalLinks(newArticle, host, scope)


# getInternalLinks('', 'http://www.siguoya.name', '/')

# 获取网站中所有外链的列表
externalLinks = set()


def getExternalLinks(pageUrl):
    html = urlopen(pageUrl)
    bsobj = BeautifulSoup(html, 'html.parser')
    links = bsobj.findAll('a', {'href': re.compile('^[http|https]((?!(siguoya)).)*$')})
    for link in links:
        if link.attrs['href'] not in externalLinks:
            externalLinks.add(link.attrs['href'])
            print(link.attrs['href'])
    print('外链的数量共有:' + str(len(externalLinks)))

# getExternalLinks('http://www.siguoya.name')

# 分离地址
def splitAddress(address):
    print(address.replace('http://', '').split('/'))
