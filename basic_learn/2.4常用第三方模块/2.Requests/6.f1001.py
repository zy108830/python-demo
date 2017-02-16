import requests, json, mysql.connector, time, random
from config import config
from requests.packages import urllib3
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString
from  selenium import webdriver


class F1000(object):
    def __init__(self):
        urllib3.disable_warnings()
        self.conn = mysql.connector.connect(user='root', password='', database='f1000')
        self.cursor = self.conn.cursor(buffered=True)
        self.header = {'HOST': 'f1000.com', 'Origin': 'https://f1000.com',
                       'Referer': 'https://f1000.com/prime/recommendations',
                       'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/55.0.2883.95 Safari/537.36'}
        self.session = requests.session()

    def try_loin(self):
        self.session.get('https://f1000.com/prime/signin?target=%2Fprime%2Frecommendations', headers=self.header,
                         verify=False)
        resp = self.session.post('https://f1000.com/security_check',
                                 {'target': '/prime/recommendations', 'j_username': config.f1000_account['username'],
                                  'j_password': config.f1000_account['password'],
                                  '_spring_security_remember_me': 'on'})
        print(resp.status_code)
        self.start_crawl()

    def write_article_record(self, article):
        self.cursor.execute(
            'INSERT INTO article (article_title,article_link,article_score,article_publish_time,article_recommendation_count,article_page) VALUES (%s,%s,%s,%s,%s,%s)',
            [
                article['article_title'],
                article['article_link'],
                article['article_score'],
                article['article_publish_time'],
                article['article_recommendation_count'],
                article['article_page']
            ])
        self.conn.commit()

    def write_recommendation_record(self):
        pass

    def start_crawl(self):
        for page in range(4477, 7200):
            time.sleep(random.randint(1, 3))
            resp = self.session.get('https://f1000.com/prime/recommendations?page=' + (str)(page), verify=False)
            # 如果DOM中存在<li><li></li><li>这种问题，chrome可以自动修正，但是爬虫会gg，此时需要通过其他选择器来达到目的
            article_badges = BeautifulSoup(resp.text, 'lxml').select('.article-badges')
            # class在Python中属于关键字，需要写成class_
            for article_badge in article_badges:
                article = {}
                # 在Python中，标签的下一个相邻标签都不会是标签类型，而是两个标签之间的空字符串或换行节点
                article_datail = \
                    article_badge.find_next_siblings(class_="articleDetails article-list-wide small-overlay")[0]
                article_title = article_datail.select('.article-title-wrapper a')
                article['article_title'] = article_title[0].text.strip()
                article['article_link'] = article_title[0]['href']
                article['article_score'] = (int)(article_badge.select('.articleFactor')[0].text)
                article['article_publish_time'] = article_datail.select('.pubdate')[0].text
                article['article_recommendation_count'] = (int)(
                    article_datail.select('.detail-type a')[0].text.replace(' Recommendations', '').replace(
                        ' Recommendation', ''))
                article['article_page'] = (int)(page)
                self.write_article_record(article)
f1000 = F1000()
f1000.try_loin()
