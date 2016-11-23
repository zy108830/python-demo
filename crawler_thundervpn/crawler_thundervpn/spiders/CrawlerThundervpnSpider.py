# -*- coding: utf-8 -*-
import scrapy
from crawler_thundervpn.items import CrawlerThundervpnItem


class CrawlerThundervpn(scrapy.Spider):
    name = "crawler_thundervpn"
    allowed_domains = ["thundervpn.tech"]
    start_urls = [
        'https://thundervpn.tech/code'
    ]

    def parse(self, response):
        for sel in response.css('tbody a::attr(href)'):
            item = CrawlerThundervpnItem()
            item['email'] = 111
            item['password'] = 222
            item['inviteCode'] = sel.extract()
            yield item
