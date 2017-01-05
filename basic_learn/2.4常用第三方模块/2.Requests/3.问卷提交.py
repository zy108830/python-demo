import requests, json, sys, time
from bs4 import BeautifulSoup


class Wenjuan(object):
    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = ''

    def submit(self):
        # 获取问卷
        res = self.session.get('http://www.psy-1.com/mob/home/wenjuan/100')
        soup = BeautifulSoup(res.text, 'lxml')
        self.csrf_token = soup.select('meta[name="csrf-token"]')[0]['content']
        res=self.session.post('http://www.psy-1.com/mob/home/wenjuan/ans',{
            'qid':100,
            'choice':'000000001000',
            'mark':4
        },headers={
            'X-CSRF-TOKEN':self.csrf_token
        })
        print(res.text)

wenjuan = Wenjuan()
wenjuan.submit()
