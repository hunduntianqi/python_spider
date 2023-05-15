# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl
from itemadapter import ItemAdapter


class TencentcareerPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['job_name', 'job_address', 'job_type', 'job_time', 'job_responsibility', 'job_requirement'])

    def process_item(self, item, spider):
        self.sheet.append([item['job_name'], item['job_address'], item['job_type'], item['job_time'],
                           item['job_responsibility'], item['job_requirement']])
        return item

    def close_spider(self, spider):
        word = input('请输入您要保存文件的关键字:')
        self.wb.save('./腾讯招聘{}相关职位.xlsx'.format(word))
        self.wb.close()
