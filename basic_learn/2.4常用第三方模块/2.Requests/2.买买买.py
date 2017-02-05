import requests, json,sys,time
from bs4 import BeautifulSoup

file = open(sys.path[0] + '/config.json', 'r')
config = json.loads(file.read())

class Buy(object):
    def __init__(self):
        self.price = {
            'paw': '',
            'mobileSSD': '',
            '1pwd':''
        }

    def get_paw_price(self):
        res = requests.get('https://paw.cloud/')
        soup = BeautifulSoup(res.text, 'lxml')
        labels = soup.select('.btn-purchase-label')
        self.price['paw'] = str.replace(str.strip(labels[1].text),'Buy Paw for ','')

    def get_samsung_ssd_price(self):
        res = requests.get(
            'https://p.3.cn/prices/get?type=1&area=19_1601_3634&pdtk=&pduid=349952081&pdpin=245165558-998015&pdbp=0&skuid=J_2376036',
            headers={
                'HOST': 'p.3.cn',
                'Referer': 'https://search.jd.com/Search?keyword=%E7%A7%BB%E5%8A%A8ssd&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%A7%BB%E5%8A%A8ssd&psort=3&click=0',
                'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
            })
        goods = json.loads(res.text)
        try:
            #m是厂家指导价
            info = '三星移动SSD的京东原价是' + goods[0]['op']+'，秒杀价是'+goods[0]['p']
            self.price['mobileSSD'] = info
        except:
            self.send_error('京东价格数据解析出错：'+res.text)


    def get_1pwd_price(self):
        res=requests.get('https://itunes.apple.com/us/app/1password-password-manager/id568903335?mt=8')
        soup=BeautifulSoup(res.text,'lxml')
        self.price['1pwd']=soup.select('.in-app-price')[0].text

    def send_notioce(self):
        requests.post('https://hook.bearychat.com/=bw8S2/incoming/' + config['bearychat']['token'], data={
            'payload': json.dumps({
                "text": "买买买 - " + time.strftime('%Y-%m-%d %X', time.localtime()),
                "markdown": False,
                "channel": "生活琐事",
                "attachments": [
                    {
                        "title": "价格监控",
                        "text": json.dumps(self.price,ensure_ascii=False)
                    }
                ]
            })
        })

    def send_error(self,error_msg):
        requests.post('https://hook.bearychat.com/=bw8S2/incoming/' + config['bearychat']['token'], data={
            'payload': json.dumps({
                "text": "买买买 - " + time.strftime('%Y-%m-%d %X', time.localtime()),
                "markdown": False,
                "channel": "生活琐事",
                "attachments": [
                    {
                        "title": "错误捕获",
                        "text": error_msg
                    }
                ]
            })
        })

buy = Buy()
buy.get_paw_price()
buy.get_samsung_ssd_price()
buy.get_1pwd_price()
buy.send_notioce()
