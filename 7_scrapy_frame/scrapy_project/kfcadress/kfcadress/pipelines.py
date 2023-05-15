# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl
from itemadapter import ItemAdapter


class KfcadressPipeline:

    def __init__(self):
        # 创建工作簿
        self.wb = openpyxl.Workbook()
        # 定位活动工作表
        self.sheet = self.wb.active
        # 写入表头信息
        self.sheet.append(['rownum', 'storeName', 'addressDetail', 'pro', 'cityName', 'provinceName'])
    def process_item(self, item, spider):
        self.sheet.append([item['rownum'], item['storeName'], item['addressDetail'], item['pro'],
                           item['cityName'], item['provinceName']])
        return item

    def close_spider(self, spider):
        city = input('请输入城市信息:')
        self.wb.save('./{}肯德基门店信息.xlsx'.format(city))
        self.wb.close()
