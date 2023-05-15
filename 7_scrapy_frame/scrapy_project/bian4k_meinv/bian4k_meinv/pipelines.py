# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class Bian4KMeinvPipeline(ImagesPipeline):

    # def process_item(self, item, spider):
    #     return item

    # 重写get_media_requests(self, item, info)方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image_url'], meta={'name': item['name']})

    # 重写file_path方法, 处理文件路径及文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        filename = request.meta['name'] + '.jpg'
        return filename

    def item_completed(self, results, item, info):
        pass
