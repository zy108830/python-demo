# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerXinli001Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    link=scrapy.Field()
    author = scrapy.Field()
    view = scrapy.Field()
    favour=scrapy.Field()
    label=scrapy.Field()
    collect=scrapy.Field()
    creat_time=scrapy.Field()
    content=scrapy.Field()
