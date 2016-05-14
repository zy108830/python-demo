from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# set是一组key的集合
pages = set()

def getLinks(pageUrl):
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bsobj = BeautifulSoup(html, 'html.parser')
    links = bsobj.findAll('a', {'href': re.compile('^/wiki/')})
    for link in links:
        if link.attrs['href'] not in pages:
            newArticle = link.attrs['href']
            pages.add(newArticle)
            print(newArticle)
            getLinks(newArticle)
getLinks('')
