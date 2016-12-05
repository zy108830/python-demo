# -*- coding: utf-8 -*-
import scrapy, time, random
from crawler_zhuankeba.items import CrawlerZhuankebaItem


class CrawlerZhuankebaSpider(scrapy.Spider):
    name = "crawler_zhuankeba"
    allowed_domains = ["zuanke8.com"]
    start_urls = [
        # 71500是最新注册的用户
        'http://www.zuanke8.com/home.php?mod=space&uid=1&do=profile'
    ]
    uid = 71501

    def parse(self, response):
        for sel in response.css('.bm_c.u_profile'):
            if sel:
                item = CrawlerZhuankebaItem()
                item['uid'] = sel.css('.xw0::text').extract()[0].replace("(UID: ", "").replace(")", "")
                item['username'] = sel.css('.mbn::text').extract()[0].strip()
                item['visit_count'] = self.parse_view_count(sel.css('.xi1::text').extract())
                item['friend_count'] = sel.css('ul.bbda a::text')[0].extract().replace(u'\u597d\u53cb\u6570 ', '')
                item['article_count'] = sel.css('ul.bbda a::text')[1].extract().replace(u'\u65e5\u5fd7\u6570 ', '')
                item['reply_count'] = sel.css('ul.bbda a::text')[2].extract().replace(u'\u56de\u5e16\u6570 ', '')
                item['theme_count'] = sel.css('ul.bbda a::text')[3].extract().replace(u'\u4e3b\u9898\u6570 ', '')
                item['score'] = response.css('#psts li::text')[1].extract()
                item['guoguo'] = response.css('#psts li::text')[2].extract().strip()
                yield item
        while self.uid <= 715600:
            self.uid += 1
            yield scrapy.Request(url="http://www.zuanke8.com/home.php?mod=space&uid=" + str(self.uid) + "&do=profile")

    def parse_view_count(self, count):
        if count:
            return count[0]
        else:
            return '0'
