import re
from ..items import PptxiazaiItem
import bs4
import scrapy


class PptxiazaiSpider(scrapy.Spider):
    name = 'pptxiazai'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['https://www.1ppt.com/xiazai']

    def parse(self, response):
        regex = '<a href="(.*?)">(.*?)</a>'
        res = response.xpath('/html/body/div[4]/div/ul//a')
        a_list = res.extract()
        for link in a_list:
            pattern = re.compile(regex, re.S)
            href = 'https://www.1ppt.com' + pattern.findall(link)[0][0]
            ppt_type = pattern.findall(link)[0][1]
            print(ppt_type, href)
            yield scrapy.Request(url=href, callback=self.erji_parse, meta={'type': ppt_type, 'type_link':href})

    def erji_parse(self, response):
        regex = '<h2><a href="(.*?)" target="_blank">(.*?)</a></h2>'
        pattern = re.compile(regex, re.S)
        ppt_link = pattern.findall(response.text)
        ppt_type = response.meta['type']
        for link in ppt_link:
            print(link)
            href = 'https://www.1ppt.com/' + link[0]
            yield scrapy.Request(url=href, callback=self.sanji_parse, meta={'type': ppt_type})
        a_next = bs4.BeautifulSoup(response.text, 'lxml').find(class_="pages").find_all('a')[-2]
        print(a_next)
        if a_next.text == '下一页':
            next_link = response.meta['type_link'] + a_next['href']
            print(next_link)
            yield scrapy.Request(url=next_link, callback=self.erji_parse, meta={'type': ppt_type, 'type_link':response.meta['type_link']})


    def sanji_parse(self, response):
        link = 'https://www.1ppt.com' + bs4.BeautifulSoup(response.text, 'lxml').find(class_="downurllist").find('a')[
            'href']
        print(link)
        yield scrapy.Request(url=link, callback=self.down_parse, meta={'type': response.meta['type']})

    def down_parse(self, response):
        item = PptxiazaiItem()
        down_link = bs4.BeautifulSoup(response.text, 'lxml').find(class_="c1").find('a')['href']
        ppt_nmae = bs4.BeautifulSoup(response.text, 'lxml').find(class_="downloadpage").find('h1').text
        print(down_link, ppt_nmae)
        item['ppt_type'] = response.meta['type']
        item['ppt_name'] = ppt_nmae
        item['ppt_link'] = down_link
        yield item


