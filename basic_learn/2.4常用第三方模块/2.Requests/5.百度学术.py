import requests, json, mysql.connector, time
from bs4 import BeautifulSoup
from  selenium import webdriver


class BDXS(object):
    def __init__(self):
        self.conn = mysql.connector.connect(user='forge', password='forge', database='baidu_xueshu')
        self.cursor = self.conn.cursor(buffered=True)
        self.header = {'HOST': 'xueshu.baidu.com',
            'Referer': 'http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_search&query=&language=1',
            'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.95 Safari/537.36'}

    def get_all_journal(self):
        for page in range(1, 115):
            resp = requests.get('http://xueshu.baidu.com/usercenter/data/journal?query=&language=1&page=' + (str)(page))
            soup = BeautifulSoup(resp.text, 'lxml')
            journal_list = soup.select('.journal_detail')
            for journal in journal_list:
                self.deal_journal_object(journal)

    def get_all_journal_records(self):
        self.cursor.execute('select id,journal_id from journal')
        return self.cursor.fetchall()

    def get_all_articles(self):
        journal_records = self.get_all_journal_records()
        journal_detail = self.get_journal_detail((str)(journal_records[0][1]))
        soup = BeautifulSoup(journal_detail, 'lxml')
        article_soupes = soup.select('.result')
        for article_soup in article_soupes:
            article={}
            article['article_journal_id']=journal_records[0][0]
            article['article_title']=article_soup.select('.res-title')[0].text
            article['article_attach_json']=article_soup.select('.relevant')[0]['data_link']
            self.cursor.execute('INSERT INTO article(article_journal_id,article_title) VALUES (%s,%s)',[article['article_journal_id'],article['article_title']])
            self.conn.commit()
            self.write_attach_record(self.cursor.lastrowid,article['article_attach_json'])

    def write_attach_record(self,article_id,attach_json):
        attach_list=json.loads(attach_json)
        print(attach_list)
        self.cursor.execute('INSERT INTO attach(attach_article_id,attach_link) VALUES (%s,%s)',[article_id,'13131'])

    def get_journal_detail(self, journal_id):
        driver = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/2.1.1/bin/phantomjs')
        driver.get('http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_page&entity_id=' + journal_id)
        time.sleep(2)
        page_source = driver.page_source
        driver.close()
        return page_source

    def deal_journal_object(self, journal_soup):
        journal_object = {}
        factors = journal_soup.select('.factor')
        journal_object['journal_id'] = journal_soup.select('.journal_img')[0]['href'].replace(
            '/usercenter/data/journal?cmd=journal_page&entity_id=', '')
        journal_object['journal_cover'] = journal_soup.select('img')[0]['src']
        journal_object['journal_title'] = journal_soup.select('.journal_title')[0].text
        journal_object['journal_factor'] = (float)(factors[0].text)
        journal_object['journal_use'] = (int)(factors[1].text)
        journal_object['journal_search'] = (int)(factors[2].text)
        journal_object['journal_publish'] = (int)(factors[3].text)
        self.write_journal_record(journal_object)

    def write_journal_record(self, journal_object):
        self.cursor.execute(
            'INSERT INTO journal (journal_id,journal_cover,journal_title,journal_factor,journal_search,journal_use,'
            'journal_publish) VALUE (%s,%s,%s,%s,%s,%s,%s)',
            [journal_object['journal_id'], journal_object['journal_cover'], journal_object['journal_title'],
                journal_object['journal_factor'], journal_object['journal_use'], journal_object['journal_search'],
                journal_object['journal_publish'], ])
        self.conn.commit()

    def close_db(self):
        self.cursor.close()
        self.conn.close()


baidu_xueshu = BDXS()
baidu_xueshu.get_all_articles()