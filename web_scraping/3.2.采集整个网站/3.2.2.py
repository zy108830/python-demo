from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# set是一组key的集合
pages = set()

def getLinks(pageUrl):
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bsobj = BeautifulSoup(html, 'html.parser')
    try:
        print('此页面标题:'+bsobj.find('h1').get_text())
    except AttributeError:
        print('无法获取页面标题')
    links = bsobj.findAll('a', {'href': re.compile('^/wiki/')})
    for link in links:
        if link.attrs['href'] not in pages:
            newArticle = link.attrs['href']
            pages.add(newArticle)
            print('新页面:'+newArticle)
            getLinks(newArticle)


getLinks('')
