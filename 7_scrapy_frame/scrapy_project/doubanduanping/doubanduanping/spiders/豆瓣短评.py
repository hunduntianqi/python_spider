import bs4
import scrapy

from ..items import DoubanduanpingItem


class Doubanduanping(scrapy.Spider):
    name = 'doubanduanping'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for i in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        start_urls.append(url)

    def parse(self, response):
        url_list = []
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        url_data = bs.find_all('a', class_="nbg")
        for ul in url_data:
            url1 = ul['href']
            for i in range(10):
                url2 = url1 + 'comments/?start={}&limit=20&status=P&sort=new_score'.format(i * 20)
            yield scrapy.Request(url2, callback=self.parse_data)

    def parse_data(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        item = DoubanduanpingItem()
        item['name'] = bs.find(class_="pl2 side-bar-link").text.strip()
        datas = bs.find_all(class_="comment-item")
        for data in datas:
            item['compent_id'] = data.find('a')['title']
            item['compent_content'] = data.find(class_="short").text
            yield item
