import requests, json,sys,time
from bs4 import BeautifulSoup

file = open(sys.path[0] + '/config.json', 'r')
config = json.loads(file.read())

class Buy(object):
    def __init__(self):
        self.price = {
            'paw': '',
            'mobileSSD': ''
        }

    def get_paw_price(self):
        res = requests.get('https://paw.cloud/')
        soup = BeautifulSoup(res.text, 'lxml')
        labels = soup.select('.btn-purchase-label')
        self.price['paw'] = str.strip(labels[1].text)

    def get_samsung_ssd_price(self):
        res = requests.get(
            'https://browser.gwdang.com/brwext/dp_query?permanent_id=6585d74e6b8befd86c6a7173e4d3dbac&union=union_gwdang&url=https%3A%2F%2Fitem.jd.com%2F2376036.html&site=360buy&isbn=&name=%E4%B8%89%E6%98%9F(SAMSUNG)%20T3%E7%B3%BB%E5%88%97%20500G%20%E7%A7%BB%E5%8A%A8%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98%EF%BC%88MU-PT500B%2FCN%EF%BC%89&keyword=&skeyword=&id=&price=1299&stock=1&province_id=&subsite_id=5&cat_id=670-686-693&pic=%2F%2Fimg11.360buyimg.com%2Fn5%2Fjfs%2Ft2440%2F269%2F1545921797%2F169393%2Fbc984916%2F56c28620Nbf4f59e0.jpg&userid=undefined&shop_name=&shop_addres=&cat_name=undefined&brand_string=&format=json&union=union_gwdang&version=1482373773539&from_device=chrome&crc64=1',
            headers={
                'HOST': 'browser.gwdang.com',
                'Referer': 'https://item.jd.com/2376036.html',
                'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
            })
        goods = json.loads(res.text)
        info = goods['code-server']['brand'] + goods['code-server']['clean_title'] + '的京东价格是' + goods['code-server'][
            'price']
        for store in goods['b2c']['store']:
            if store['dp_id'] == '1117284354669906-1':
                info += ', ' + store['site_name'] + '的价格是' + store['price']
        self.price['mobileSSD']=info

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
buy = Buy()
buy.get_paw_price()
buy.get_samsung_ssd_price()
buy.send_notioce()
