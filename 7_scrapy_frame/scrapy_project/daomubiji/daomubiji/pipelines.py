# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class DaomubijiPipeline:

    def __init__(self):
        try:
            os.mkdir('./盗墓笔记')
        except:
            print('盗墓笔记文件夹已存在！！')

    def process_item(self, item, spider):
        try:
            os.mkdir('./盗墓笔记/{}'.format(item['book_name']))
        except:
            print('文件夹{}已存在！！'.format(item['book_name']))
        with open('./盗墓笔记/{}/{}.txt'.format(item['book_name'], item['name'].replace('?', '')), 'w', encoding='utf-8') as file:
            file.write(item['chapter'])
        return item
