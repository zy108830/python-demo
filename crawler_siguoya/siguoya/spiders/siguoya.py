import scrapy

from siguoya.items import SiguoyaItem
class SiguoyaSpider(scrapy.Spider):
    name = 'siguoya'
    allowed_domains = ['siguoya.name']
    start_urls = [
        'http://www.siguoya.name/'
    ]
    def parse(self, response):
        items = []
        for sel in response.css('#append_new .panel-body'):
            item = SiguoyaItem()
            item['image_urls']=[]
            item["title"] = sel.css('.text-center a::text').extract()[0].replace(' ', '').replace('\n', '')
            item["img"] = sel.css('img::attr(data-original)').extract()[0]
            item["link"] = sel.css('.text-center a::attr(href)').extract()[0]
            item['image_urls'].append(item['img'])
            items.append(item)
        return  items
