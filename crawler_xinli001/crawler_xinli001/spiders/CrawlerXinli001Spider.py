# -*- coding: utf-8 -*-
import scrapy, time, numbers, random
from crawler_xinli001.items import CrawlerXinli001Item


class CrawlerXinli001Spider(scrapy.Spider):
    name = "crawler_xinli001"
    allowed_domains = ["xinli001.com"]
    start_urls = [
        'http://www.xinli001.com/info?page=1'
    ]
    nextIndex = 1

    def parse(self, response):
        for sel in response.css('#hot-list ul')[0].css('li'):
            item = CrawlerXinli001Item()
            try:
                item['title'] = sel.css('.text h2 a::text').extract()[0]
            except Exception as e:
                item['title'] = ''
            try:
                item['cover'] = sel.css('.img img::attr(src)').extract()[0]
            except Exception as e:
                item['cover'] = ''
            try:
                item['author'] = sel.css('.attr h4 a::text').extract()[0]
            except Exception as e:
                item['author'] = ''
            try:
                item['view'] = sel.css('.ico-view::text').extract()[0]
            except Exception as e:
                print("标题是"+item['title'],'==========================')
            item['favour'] = sel.css('.ico-digg::text').extract()[0]
            item['label'] = sel.css('.tag a::text').extract()
            item['link'] = sel.css('.text h2 a::attr(href)').extract()[0]
            request = scrapy.Request(url=item['link'], callback=self.getArticleDetail)
            request.meta['item'] = item
            yield request
        while self.nextIndex <= 1372:
            time.sleep(random.randint(1, 5))
            self.nextIndex += 1
            print("http://www.xinli001.com/info?page=" + str(self.nextIndex), 'siguoya爬取页码')
            yield scrapy.Request(url="http://www.xinli001.com/info?page=" + str(self.nextIndex), callback=self.parse)

    def getArticleDetail(self, response):
        item = response.meta['item']
        item['creat_time'] = response.css('.attr span::text').extract()[0]
        item['collect'] = response.css('#favnum::text').extract()[0]
        item['content'] = response.css('.texts').extract()[0]
        return item
