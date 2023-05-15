import scrapy
from ..items import LianglipicItem
import re


class LianglipicSpider(scrapy.Spider):
    name = 'lianglipic'
    allowed_domains = ['www.hexuexiao.cn']
    keyword_1 = input('请输入图片类别1:')
    keyword_2 = input('请输入图片类别2:')
    start_urls = ['https://www.hexuexiao.cn/{}/{}/'.format(keyword_1, keyword_2)]
    num = 1
    def parse(self, response):
        print(response.text)
        regex = '<div class="waterfall_1box">.*?<a href="(.*?)" >.*?</div>'
        pattern = re.compile(regex, re.S)
        for pic_link in pattern.findall(response.text):
            print(pic_link)
            yield scrapy.Request(url=pic_link, callback=self.pic_parse)
        if "next_a" in response.text:
            regex_next = '<a class="next_a" href="(.*?)">'
            pattern_next = re.compile(regex_next, re.S)
            next_link = pattern_next.findall(response.text)[0]
            yield scrapy.Request(url=next_link, callback=self.parse)
        pass

    def pic_parse(self, response):
        item = LianglipicItem()
        regex_img = '<img class="img-responsive center-block" src="(.*?)"/>'
        pattern = re.compile(regex_img, re.S)
        link = pattern.findall(response.text)[0]
        print(link)
        name = link.split('/')[-1]
        item['name'] = name
        item['link'] = link
        item['num'] = self.num
        yield item
        print(link)
        if "next_main_img" in response.text:
            self.num += 1
            regex_next = '<a class="next_main_img" href="(.*?)">'
            pattern_next = re.compile(regex_next, re.S)
            next_link = 'https://www.hexuexiao.cn' + pattern_next.findall(response.text)[0]
            yield scrapy.Request(url=next_link, callback=self.pic_parse)
        pass
