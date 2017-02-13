import requests, mysql.connector
from  requests.packages import urllib3


class Zhihu(object):
    def __init__(self):
        urllib3.disable_warnings()
        self.header = {'HOST': 'www.zhihu.com', 'Referer': 'https://www.zhihu.com/people/ipreacher/answers',
            'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.95 Safari/537.36'}
        self.session = requests.session()
        self.session.get('https://www.zhihu.com/', headers=self.header, verify=False)

    def get_train_users(self, page, count):
        conn = mysql.connector.connect(user='forge', password='forge', database='train12306')
        cursor = conn.cursor(buffered=True)
        cursor.execute('select * from train_user limit ' + (str)(page * count) + ',' + (str)(count))
        records = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return records

    def get_train_record(self):
        pass

    def valid_user_exist(self, nickname):
        resp = self.session.get('https://www.zhihu.com/people/' + nickname + '/answers', headers=self.header,
            verify=False)
        return resp.status_code


zh = Zhihu()
train_users = zh.get_train_users(0, 1000)
for train_user in train_users:
    status_code = (int)(zh.valid_user_exist(train_user[5]))
    if status_code != 404:
        print(train_user[5])