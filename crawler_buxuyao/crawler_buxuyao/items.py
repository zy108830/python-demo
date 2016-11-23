# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BuxuyaoItem(scrapy.Item):
    title = scrapy.Field()
    cover = scrapy.Field()
    intro = scrapy.Field()
    pageLink=scrapy.Field()
    detailLink=scrapy.Field()
    detailImg=scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
