import requests
from bs4 import BeautifulSoup
import json, time
class Unicom():
    def __init__(self, user, passwd):
        self.session = requests.session()
        self.overview = {
            'user_name': '',
            'package_name': ''
        }
        self.fees = {}
        self.traffic = {}
        self.bills = {}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        self.login(user, passwd)


    def login(self, user, passwd):
        data = {
            'app_code': 'ECS-YH-WAP',
            'user_id': user,
            'user_pwd': passwd,
            'user_type': '01',
            'pwd_type': '01',
            'display': 'web',
            'response_type': 'code',
            'redirect_uri': 'http://wap.10010.com/t/loginCallBack.htm',
            'is_check': '1',
            'state': 'http://wap.10010.com/t/myunicom.htm'
        }
        html = self.session.post('https://uac.10010.com/oauth2/new_auth?req_time=1471066271174', data=data,
                                 headers=self.headers, verify=False).text
        try:
            code = json.loads(html)['code']
        except:
            print('Login Failed!')
            return
        print('http://wap.10010.com/t/loginCallBack.htm?code=%s' % code)
        # 登录成功之后的回调
        html = self.session.get('http://wap.10010.com/t/loginCallBack.htm?code=%s' % code, headers=self.headers,
                                verify=False).text

    def query_fees(self):
        # html = self.session.get('http://wap.10010.com/t/query/queryRealTimeFeeInfoNew.htm', headers=headers,verify=False).text
        html = self.session.get(
            'http://wap.10010.com/t/query/queryBalanceNew.htm?menuId=000200010002&mobile_c_from=null', headers=self.headers,
            verify=False).text
        # html = self.session.get('http://wap.10010.com/t/operationservice/queryOcsPackageFlowLeft.htm?menuId=000200020004&mobile_c_from=null', headers=headers,verify=False).text

        soup = BeautifulSoup(html, "lxml")
        overview = soup.find('div', class_="clientInfo4_list").find_all('span')
        self.overview['user_name'] = overview[1].text
        self.overview['package_name'] = overview[3].text

        balance = soup.find('div', class_="cridit_list").find_all('span')
        self.fees['balance_total'] = balance[0].text
        self.fees['balance_available'] = balance[1].text
        self.fees['balance_frozen'] = balance[8].text

        return self.fees

    def query_traffic(self):
        html = self.session.get(
            'http://wap.10010.com/mobileService/operationservice/queryOcsPackageFlowLeftContent.htm',
            headers=self.headers, verify=False).text
        traffic = BeautifulSoup(html, "lxml").find('div', class_='flowpackageList5').find_all('span')
        self.traffic['traffice_balance_now'] = str.strip(traffic[0].text)
        self.traffic['traffice_balance_last'] = str.strip(traffic[3].text)
        return self.traffic

    def query_bills(self):
        html = self.session.get(
            'http://wap.10010.com/mobileService/query/queryRealFeeHistroyDetail.htm?desmobile=&version=wap@4.0&menuId=000200010005&month=&randm=0.2278361300073266',
            headers=self.headers, verify=False).text
        bills = BeautifulSoup(html, "lxml").select('.detailL')

        for item in bills:
            self.bills[str.strip(item.find('th').text)] = str.replace(item.find('td').text, ' 元', '')
        return self.bills

file = open('./config.json', 'r')
config=json.loads(file.read())

unicom = Unicom(config['siguoya']['mobile']['number'], config['siguoya']['mobile']['password'])

requests.post('https://hook.bearychat.com/=bw8S2/incoming/'+config['bearychat']['token'], data={
    'payload': json.dumps({
        "text": "联通话费账单监控 - " + time.strftime('%Y-%m-%d %X', time.localtime()),
        "markdown": False,
        "channel": "生活琐事",
        "attachments": [
            {
                "title": "思过崖的账单",
                "text": "话费余额：" + str(unicom.query_fees()) + "，流量余额：" + str(unicom.query_traffic()) + "，账单详情：" + str(
                    unicom.query_bills())
            }
        ]
    })
})
