# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_num=scrapy.Field()
    book_name=scrapy.Field()
    book_author=scrapy.Field()
    book_price=scrapy.Field()
    pass
