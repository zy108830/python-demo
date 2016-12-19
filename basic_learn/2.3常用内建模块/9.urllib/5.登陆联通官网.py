from urllib import request, parse
from bs4 import BeautifulSoup
import re, json, time


class ChinaUnicom(object):
    def __init__(self, mobile, password):
        self._mobile = mobile
        self._password = password
        self._login_cookies = '',
        self._search_cookies = '',
        self.User_Agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

        self._Host='iservice.10010.com'
        self._Origin='http://iservice.10010.com'
        self._Pragma='no-cache'
        self._Referer='http://iservice.10010.com/e4/index_server.html'

    def user_login(self):
        login_ulr = 'https://uac.10010.com/portal/Service/MallLogin?callback=jQuery17201382940401299657_1482046368553&req_time=' + str(
            int(
                time.time() * 1000)) + '&redirectURL=http://www.10010.com&userName=' + self._mobile + '&password=' + self._password + '&pwdType=01&productType=01&redirectType=01&rememberMe=1&_=' + str(
            int(time.time() * 1000))
        req=request.Request(login_ulr)
        req.add_header('User-Agent', self.User_Agent)
        print(login_ulr)
        with request.urlopen(req) as f:
            data = f.read()
        index = str.find(data.decode('utf-8'), 'resultCode:"0000"')
        if index > -1:
            self._set_login_cookie(self._extract_cookies(f.getheaders()))
            return True
        else:
            print(data)
            return False

    def login_success(self):
        print('登陆成功,good job !')
        pass

    def login_failure(self):
        print('登录失败,over...')
        pass

    def get_user_info(self):
        request_data = parse.urlencode({}).encode('utf-8')
        req = request.Request(
            'http://iservice.10010.com/e3/static/query/accountBalance/search?_='+str(int(time.time() * 1000))+'&accessURL=http://iservice.10010.com/e4/skip.html?menuCode=000100010002&menuCode=000100010002&menuid=000100010013')
        search_cookie=self._get_search_cookie()
        print('search_cookie',search_cookie)
        time.sleep(2)
        # req.add_header('Cookie', 'route=5eedb21b90a922c9b5a2ce53582667c0;e3=sZkJYXsfwPg94GVQY3ky0jMXGsmXHY1b5y3MplVVrZBt29w08nSC!-95466647;')
        req.add_header('Cookie', search_cookie)
        req.add_header('User-Agent', self.User_Agent)

        with request.urlopen(req, request_data) as f:
            print(f.read())

    def _set_login_cookie(self, cookies):
        self._login_cookies = cookies
        pass

    def _get_login_cookie(self):
        return self._login_cookies
        pass

    def _set_search_cookie(self, cookies):
        self._search_cookies = cookies
        pass

    def _get_search_cookie(self):
        auth_url = 'http://iservice.10010.com/e3/static/query/searchPerInfoDetail/?_=' + str(int(time.time() * 1000))
        print(auth_url)

        req = request.Request(auth_url)
        req.add_header('Cookie', self._login_cookies)
        req.add_header('User-Agent', self.User_Agent)
        req.add_header('Host', self._Host)
        req.add_header('Origin', self._Origin)
        req.add_header('Pragma', self._Pragma)
        req.add_header('Referer', self._Referer)

        login_data = parse.urlencode({}).encode('utf-8')
        with request.urlopen(req, login_data) as f:
            self._set_search_cookie(self._extract_cookies(f.getheaders()))
            return self._search_cookies

    def _extract_cookies(self, headers):
        cookie_str = ''
        for k, v in headers:
            if k == 'Set-Cookie':
                cookie_str += re.sub(';.*', '', v) + ';'
        return cookie_str


cu = ChinaUnicom('手机号', '密码')
loginRes = cu.user_login()
if loginRes:
    cu.login_success()
    print(cu.get_user_info())
else:
    cu.login_failure()
