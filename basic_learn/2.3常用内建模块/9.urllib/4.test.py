import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}


class Unicom():
    def __init__(self,user,passwd):
        self.session=requests.session()
        self.login(user,passwd)

    def login(self,user,passwd):
        data={
        'app_code':'ECS-YH-WAP',
        'user_id':user,
        'user_pwd':passwd,
        'user_type':'01',
        'pwd_type':'01',
        'display':'web',
        'response_type':'code',
        'redirect_uri':'http://wap.10010.com/t/loginCallBack.htm',
        'is_check':'1',
        'state':'http://wap.10010.com/t/myunicom.htm'
        }
        html=self.session.post('https://uac.10010.com/oauth2/new_auth?req_time=1471066271174',data=data,headers=headers).text
        try:
            code=json.loads(html)['code']
        except:
            print('Login Failed!')
            return
        html=self.session.get('http://wap.10010.com/t/loginCallBack.htm?code=%s'%code,headers=headers).text

    def query_realtimefee(self):
        html=self.session.get('http://wap.10010.com/t/query/queryRealTimeFeeInfoNew.htm',headers=headers).text
        soup=BeautifulSoup(html,'lxml')
        clientInfo4_list=soup.find('div',{'class':'clientInfo4_list'}).find_all('li')
        result={}
        for li in clientInfo4_list:
            spans=li.find_all('span')
            result[spans[0].get_text().replace('：','')]=spans[1].get_text()
        cridit_list=soup.find('div',{'class':'cridit_list'})
        for item in cridit_list.find_all('div',{'class':'borderB_d2'}):
            try:
                key=item.find('div',{'class':'fl'}).get_text().replace('\r','').replace('\n','').replace('\t','')
                value=item.find('div',{'class':'fr'}).get_text().replace('\r','').replace('\n','').replace('\t','')
                result[key]=value
            except:
                continue
        return result

    def query_package(self):
        html=self.session.get('http://wap.10010.com/mobileService/operationservice/queryOcsPackageFlowLeftContent.htm',headers=headers).text
        table=BeautifulSoup(html,'lxml').find_all('div',{'class':'flow4g_list'})
        result={'packages':[]}
        for item in table:
            try:
                name=item.find('p').get_text().replace('\r','').replace('\n','').replace('\t','')
                allvalue=item.find('dd').get_text().replace('\r','').replace('\n','').replace('\t','').replace('xa0297','').replace('\xa0','')
                value=item.find('dt').get_text().replace('\r','').replace('\n','').replace('\t','').replace('xa0297','').replace('\xa0','')
            except:
                continue
            result['packages'].append({'name':name,'all':allvalue,'value':value})
        return result