import scrapy
import bs4
from..items import DangdangwangItem

class Dangdangwang(scrapy.Spider):
    name='dangdangwang'
    allowed_domains = ['bang.dangdang.com/']
    start_urls = []
    for m in range(25):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-{}'.format(m+1)
        start_urls.append(url)
        def parse(self,response):
            item=DangdangwangItem()
            bs = bs4.BeautifulSoup(response.text, 'html.parser')
            # 用BeautifulSoup解析response。
            num = bs.find_all(class_="list_num")
            # print(num)
            name = bs.find_all(class_="name")
            author = bs.find_all(class_="publisher_info")
            # print(author)
            price = bs.find_all(class_="price_r")
            m = 0
            for i in range(20):
                item['book_num'] = num[i].text
                item['book_name'] = name[i].find('a')['title']
                item['book_author'] = author[m].find('a')['title']
                item['book_price'] = price[i].text
                m += 2
                print(item['book_name'])
                # 打印书名。
                yield item
                # yield item是把获得的item传递给引擎。