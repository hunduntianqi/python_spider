# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl

class DoubanduanpingPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        # 创建工作薄
        self.sheet = self.wb.active
        # 定位活动表
        self.sheet.append(['书名', '评论人员昵称', '短评内容'])
    def process_item(self, item, spider):
        line=[item['name'],item['compent_id'],item['compent_content']]
        self.sheet.append(line)
        return item
    def close_spider(self,spider):
        self.wb.save(input('请输入保存文件名称:')+'.xlsx')
        self.wb.close()
