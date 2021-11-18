import scrapy


class ScrpZhishikooSpider(scrapy.Spider):
    name = 'scrp_zhishikoo'
    allowed_domains = ['https://book.zhishikoo.com/']
    start_urls = ['http://https://book.zhishikoo.com//']

    def parse(self, response):
        pass
