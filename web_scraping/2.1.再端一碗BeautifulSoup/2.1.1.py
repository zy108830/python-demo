from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.buxuyao.cn/')
bsobj = BeautifulSoup(html, 'html.parser')

# print(bsobj)
sentences = bsobj.find("ul", {"class": "e2"}).findAll('a', {'class': 'title'})

arr=[]

for sentence in sentences:
    d = {}
    d['text'] = sentence.get_text()
    d['link'] = sentence['href']
    arr.append(d)

print(arr)
