# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

"""
    Scrapy Item类可以自定义爬取字段, 爬虫文件中对Item实例化后, 会有方法将数据交给管道文件处理
    相当于定义字典只定义了key, 没有对应的值
"""
import scrapy


class ScrapyexplainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 字段定义示例
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    pass
