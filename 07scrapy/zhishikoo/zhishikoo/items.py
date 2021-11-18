# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhishikooItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = "zhishikoo"
    allowed_domains = ["zhishikoo.com"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    pass
