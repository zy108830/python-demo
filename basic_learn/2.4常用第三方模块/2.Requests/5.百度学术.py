import requests,json,mysql.connector,time
from bs4 import BeautifulSoup
from  selenium import webdriver


class BDXS(object):
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='', database='baidu_xueshu')
        self.cursor = self.conn.cursor(buffered=True)

    def get_all_journal(self):
        for page in range(1, 115):
            resp = requests.get('http://xueshu.baidu.com/usercenter/data/journal?query=&language=1&page='+(str)(page))
            soup = BeautifulSoup(resp.text, 'lxml')
            journal_list = soup.select('.journal_detail')
            for journal in journal_list:
                self.deal_journal_object(journal)

    def get_all_journal_records(self):
        self.cursor.execute('select journal_id from journal')
        return  self.cursor.fetchall()

    def get_all_articles(self):
        journal_records=self.get_all_journal_records()
        journal_detail=self.get_journal_detail((str)(journal_records[0]))
        print(journal_detail)

    def get_journal_detail (self,journal_id):
        driver=webdriver.PhantomJS(executable_path='/usr/local/phantomjs/2.1.1/bin/phantomjs')
        driver.get('http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_page&entity_id=' + journal_id)
        time.sleep(5)
        page_source=driver.page_source
        driver.close()
        return  page_source

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

    def write_journal_record(self,journal_object):
        self.cursor.execute('INSERT INTO journal (journal_id,journal_cover,journal_title,journal_factor,journal_search,journal_use,journal_publish) VALUE (%s,%s,%s,%s,%s,%s,%s)',[
            journal_object['journal_id'],
            journal_object['journal_cover'],
            journal_object['journal_title'],
            journal_object['journal_factor'],
            journal_object['journal_use'],
            journal_object['journal_search'],
            journal_object['journal_publish'],
        ])
        self.conn.commit()

    def close_db(self):
        self.cursor.close()
        self.conn.close()


baidu_xueshu = BDXS()
baidu_xueshu.get_all_articles()
