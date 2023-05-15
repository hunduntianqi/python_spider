import bs4
import scrapy
from ..items import Bian4KMeinvItem


class Bian4kmeinvSpider(scrapy.Spider):
    name = 'bian4kmeinv'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']

    def parse(self, response):
        item = Bian4KMeinvItem()
        res = bs4.BeautifulSoup(response.text, 'lxml')
        # print(res)
        a_list = res.find('ul', class_="clearfix").find_all('a')
        print(a_list)
        for a in a_list:
            pic_data = 'https://pic.netbian.com' + a['href']
            yield scrapy.Request(url=pic_data, callback=self.pic_down)
        if "下一页" in response.text:
            next_page = res.find(class_="page").find_all('a')[-1]['href']
            print(next_page)
            url = 'https://pic.netbian.com{}'.format(next_page)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def pic_down(self, response):
        item = Bian4KMeinvItem()
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        pic_url = 'https://pic.netbian.com' + soup.find(id="img").find('img')['src']
        pic_name = soup.find('div', class_="photo-hd").text
        item['image_url'] = pic_url
        item['name'] = pic_name
        yield item
