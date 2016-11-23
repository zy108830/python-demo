# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
class DownloadPipeline(object):
    def process_item(self,item, spider):
        print(item)
        return item
