# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcareerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名称 + 地址 + 类别 + 时间 + 职责 + 要求
    job_name = scrapy.Field()
    job_address = scrapy.Field()
    job_type = scrapy.Field()
    job_time = scrapy.Field()
    job_responsibility = scrapy.Field()
    job_requirement = scrapy.Field()
    pass
