import re
from ..items import DaomubijiItem
import bs4
import scrapy


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['https://www.daomubiji.com/']

    def parse(self, response):
        regex = '<p><a href="(.*?)"></p>'
        res = response.text
        pattern = re.compile(regex, re.S)
        # book_list = pattern.findall().remove(8)
        for link in pattern.findall(res):
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_erji_page)

    def parse_erji_page(self, response):
        regex = '<article class="excerpt excerpt-c3"><a href="(.*?)">'
        res = response.text
        pattern = re.compile(regex, re.S)
        for link in pattern.findall(res):
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_sanji_page)

    def parse_sanji_page(self, response):
        item = DaomubijiItem()
        res = bs4.BeautifulSoup(response.text, 'lxml')
        book_name = res.find(class_="item item-3").find('a').text
        name = res.find(class_="article-title").text
        regex = ' 第(.*?)章'
        # regex2 = '第.*?第(.*?)章'
        pattern = re.compile(regex, re.S)
        # pattern2 = re.compile(regex2, re.S)
        id_list = pattern.findall(name)
        # id_list2 = pattern2.findall(name)
        # if len(id_list2) > 0:
        #     id = id_list2[0]
        #     id_name = self.str_int_switch(id)
        #     name = name.replace(id, id_name)
        # else:
        if len(id_list) > 0:
            id = id_list[0]
            id_name = self.str_int_switch(id)
            name = name.replace('第{}章'.format(id), '第{}章'.format(id_name))
        text_all = res.find(class_="article-content").find_all('p')
        chapter = name + '\n'
        for text in text_all:
            chapter += (text.text + '\n')
        print(name)
        print(chapter)
        item['book_name'] = book_name
        item['name'] = name
        item['chapter'] = chapter
        yield item

    def str_int_switch(self, str):
        global str1, str2, str3, str4
        if len(str.split('千')) == 2:
            print(str.split('千'))
            str1 = int(str.split('千')[0][-1].replace('九', '9').replace('八', '8').replace('七', '7').replace('六',
                   '6').replace('五','5').replace('四', '4').replace('三', '3').replace('二', '2').replace('一',
                   '1').replace('零', '0')) * 1000
        else:
            str1 = 0
        if len(str.split('百')) == 2:
            print(str.split('百'))
            str2 = int(str.split('百')[0][-1].replace('九', '9').replace('八', '8').replace('七', '7').replace('六',
                   '6').replace('五', '5').replace('四', '4').replace('三', '3').replace('二', '2').replace('一',
                   '1').replace('零','0')) * 100
        else:
            str2 = 0
        if len(str.split('十')) == 2:
            if str.split('十')[0] != '':
                print(str.split('十'))
                str3 = int(str.split('十')[0][-1].replace('九', '9').replace('八', '8').replace('七',
                       '7').replace('六','6').replace('五', '5').replace('四', '4').replace('三', '3')
                       .replace('二', '2').replace('一','1').replace('零','0')) * 10
            if len(str) == 2:
                if str[0] == '十':
                    str3 = 10
        else:
            str3 = 0
        if len(str) == 1:
            str4 =int(str.replace('九', '9').replace('八', '8').replace('七','7').replace('六',
                                '6').replace('五', '5').replace('四', '4').replace('三', '3').replace('二',
                                '2').replace('一','1').replace('十', '10'))
        if len(str) != 1:
            str4 = int(str[-1].replace('九', '9').replace('八', '8').replace('七', '7').replace('六',
                   '6').replace('五','5').replace('四', '4').replace('三', '3').replace('二',
                    '2').replace('一', '1').replace('十', '0').replace('百', '0').replace('千', '0'))

        id = str1 + str2 + str3 + str4
        return id.__str__()

