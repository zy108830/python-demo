# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerZhuankebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid = scrapy.Field()
    username = scrapy.Field()
    visit_count = scrapy.Field()
    slogan = scrapy.Field()
    friend_count = scrapy.Field()
    article_count = scrapy.Field()
    reply_count = scrapy.Field()
    theme_count = scrapy.Field()
    sex = scrapy.Field()
    birth = scrapy.Field()
    web = scrapy.Field()
    introduce = scrapy.Field()
    interest = scrapy.Field()
    city = scrapy.Field()
    group = scrapy.Field()
    register_time = scrapy.Field()
    last_visit_time = scrapy.Field()
    score = scrapy.Field()
    guoguo = scrapy.Field()
