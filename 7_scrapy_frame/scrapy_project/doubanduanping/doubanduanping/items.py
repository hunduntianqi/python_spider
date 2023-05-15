# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanduanpingItem(scrapy.Item):
    name=scrapy.Field()
    compent_id=scrapy.Field()
    compent_content=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
