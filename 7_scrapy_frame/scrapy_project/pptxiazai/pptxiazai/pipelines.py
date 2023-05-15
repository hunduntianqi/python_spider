# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import os

class PptxiazaiPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['ppt_link'], meta={'item':item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['item']
        try:
            os.mkdir('./ppt/{}'.format(item['ppt_type']))
        except:
            print('文件夹{}已存在！！'.format(item['ppt_type']))
        filename = '{}/{}.{}'.format(item['ppt_type'], item['ppt_name'], item['ppt_link'].split('.')[-1])
        return filename

