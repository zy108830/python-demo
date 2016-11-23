# -*- coding: utf-8 -*-
import scrapy
from crawler_buxuyao.items import BuxuyaoItem


class BuxuyaoSpider(scrapy.Spider):
    name = "buxuyao"
    allowed_domains = ["www.buxuyao.cn"]
    start_urls = [
        'http://www.buxuyao.cn/picture/list_2_1.html'
    ]
    nextIndex = 2
    items = []

    def parse(self, response):
        for sel in response.css('.e2 li'):
            item = BuxuyaoItem()
            item['image_urls'] = []
            try:
                item['title'] = sel.css('.title::text').extract()[0]
            except Exception as e:
                item['title'] = sel.css('.title b::text').extract()[0]
            # cover = sel.css('.preview img::attr(src)').extract()[0]
            # if (cover.find('http') > -1):
            #     item['cover'] = cover
            # else:
            #     item['cover'] = 'http://www.buxuyao.cn' + cover
            # item['image_urls'].append(item['cover'])
            item['intro'] = sel.css('p.intro::text').extract()[0]
            item['pageLink'] = response.url
            item['detailLink'] = 'http://www.buxuyao.cn' + sel.css('.preview::attr(href)').extract()[0]
            request = scrapy.Request(url=item['detailLink'], callback=self.parse_detail)
            request.meta['item'] = item
            yield request
        #40表示记录所在的页码
        while self.nextIndex < 40:
            yield scrapy.Request('http://www.buxuyao.cn/picture/list_2_' + str(self.nextIndex) + '.html', self.parse)
            self.nextIndex += 1

    def parse_detail(self, response):
        item = response.meta['item']
        item['detailImg'] = response.css('.content td img::attr(src)').extract()[0]
        item['image_urls'].append(item['detailImg'])
        return item
