# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

import pymysql
from itemadapter import ItemAdapter


class ScrapyexplainPipeline:

    def __init__(self):
        self.file = open('./瓜子二手车.csv', 'w', encoding='utf-8', newline='')
        self.write = csv.writer(self.file)
        self.write.writerow(('name', 'price', 'link'))

    def open_spider(self, spider):
        """爬虫程序启动时, 只执行一次, 一般用于数据库的链接和文件对象的创建"""
    def process_item(self, item, spider):
        """对数据进行处理, 一般为写入数据库或写入对应文件对象"""
        self.write.writerow((item['name'], item['price'], item['link']))
        print(item['name'], item['price'], item['link'])
        return item

    def close_spider(self, spider):
        """爬虫程序结束时, 只执行一次, 一般用于数据库的断开和文件对象的关闭"""
        self.file.close()

# class ScrapyexplainPipeline2:
#     def __init__(self):
#         # 链接数据库
#         self.db = pymysql.connect(host='localhost', port=3306, user='root', password='13480194858gpt', database='python01')
#         # 创建游标对象
#         self.cusor = self.db.cursor()
#         self.i = 1
#
#     def process_item(self, item, spider):
#         # 向数据库中写入数据
#         sql = 'insert into guizi values(%s, %s, %s, %s)'
#         list = [self.i, item['name'], item['price'], item['link']]
#         self.cusor.execute(sql, list)
#         # 提交数据
#         self.db.commit()
#         self.i += 1
#
#     def close_spider(self, spider):
#         # 关闭游标对象和数据库链接
#         self.cusor.close()
#         self.db.close()
#
