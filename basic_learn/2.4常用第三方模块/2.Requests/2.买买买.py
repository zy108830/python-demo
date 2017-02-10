import requests, json, sys, time
from bs4 import BeautifulSoup

file = open(sys.path[0] + '/config.json', 'r')
config = json.loads(file.read())


class Buy(object):
    def __init__(self):
        self.price = {
            'mobileSSD': '',
            '1pwd': ''
        }

    def get_paw_price(self):
        res = requests.get('https://paw.cloud/')
        soup = BeautifulSoup(res.text, 'lxml')
        labels = soup.select('.btn-purchase-label')
        self.price['paw'] = str.replace(str.strip(labels[1].text), 'Buy Paw for ', '')

    def get_samsung_ssd_price(self):
        res = requests.get(
            'http://s.manmanbuy.com/Default.aspx?smallclass=0&ppid=0&siteid=&searchmode=0&f1=0&f2=0&f3=0&f4=0&f5=0&f6=0&price1=0&price2=0&orderby=score&iszy=1&istmall=0&key=MU-PT500B%2fCN',
            headers={
                'HOST': 's.manmanbuy.com',
                'Referer': 'http://s.manmanbuy.com/Default.aspx?key=MU-PT500B%2FCN&btnSearch=%CB%D1%CB%F7',
                'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
            })
        list = BeautifulSoup(res.text, 'lxml').select('.bjlineSmall')
        priceInfo = '三星移动固态硬盘: '
        for item in list:
            priceInfo += '【' + item.select('.f14proname')[0].text + item.select('.listpricespan')[0].text + '】' + \
                         item.select('.priceyouhui')[0].text + '；'
        self.price['mobileSSD'] = priceInfo

    def get_1pwd_price(self):
        res = requests.get('https://itunes.apple.com/us/app/1password-password-manager/id443987910?mt=12&ign-mpt=uo=2')
        soup = BeautifulSoup(res.text, 'lxml')
        self.price['1pwd'] = soup.select('.price')[0].text

    def send_notioce(self):
        requests.post('https://hook.bearychat.com/=bw8S2/incoming/' + config['bearychat']['token'], data={
            'payload': json.dumps({
                "text": "买买买 - " + time.strftime('%Y-%m-%d %X', time.localtime()),
                "markdown": False,
                "channel": "生活琐事",
                "attachments": [
                    {
                        "title": "价格监控",
                        "text": json.dumps(self.price, ensure_ascii=False)
                    }
                ]
            })
        })

    def send_error(self, error_msg):
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
buy.get_samsung_ssd_price()
buy.get_1pwd_price()
buy.send_notioce()
