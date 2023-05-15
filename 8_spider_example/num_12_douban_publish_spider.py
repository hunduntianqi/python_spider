"""
    豆瓣阅读出版社信息抓取
"""
import time
from pymongo import MongoClient
import requests
from pyquery import PyQuery
from lxml import etree
from datetime import datetime


class DouBanReadPublish:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'bid=29Df9Ol1X_c; douban-fav-remind=1; __gads=ID=c2390a42a1cc0261-2221da0ddad000eb:T=1646453421:RT=1646453421:S=ALNI_MaBpHAXUgZxjvjnX-K5mkhYtjuSIA; __utma=30149280.669575135.1646453404.1646453404.1646453404.1; __utmz=30149280.1646453404.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.3.669575135.1646453404; _gid=GA1.3.1929058806.1648034451; _ga=GA1.1.669575135.1646453404; _pk_ses.100001.a7dd=*; _pk_id.100001.a7dd=d677026e2b321e46.1648034453.1.1648034479.1648034453.; _ga_RXNMP372GL=GS1.1.1648034451.1.1.1648034492.19',
            'Host': 'read.douban.com',
            'Pragma': 'no-cache',
            'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
        }
        self.mongo = MongoClient('localhost', 27017)['豆瓣出版社']['豆瓣出版社信息']

    def get_publish_url(self):
        """ 解析每个出版社详情连接 """
        url = 'https://read.douban.com/provider/all'
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        # print(response.text)
        pq_parse = PyQuery(response.text)
        ul_list = pq_parse('.provider-items').items()
        publish_tuple_list = []
        for ul in ul_list:
            li_list = ul('a').items()
            for li in li_list:
                name = li(".name").text()
                publish_url = 'https://read.douban.com' + li('a').attr('href')
                publish_tuple_list.append((name, publish_url))
        return publish_tuple_list

    def get_page_url(self, publish_tuple):
        """ 解析获取单个出版社每页详情连接 """
        page_url_list = []  # 定义列表存储每页url
        publish_url = publish_tuple[1]
        response = requests.get(publish_url, headers=self.headers)
        # 实例化etree对象
        tree = etree.HTML(response.text)
        # 解析获取总页数
        try:
            page_all = int(tree.xpath('/html/body/div[1]/div[3]/section[2]/div[3]/div/ul/li')[-2].xpath('a/text()')[0])
            for i in range(page_all):
                url = publish_url + '?sort=hot&start={}'.format(i * 30)
                page_url_list.append(url)
            return page_url_list
        except:
            page_url_list.append(publish_url)
            return page_url_list

    def get_book_url(self, page_url):
        """ 解析获取每本书的详情连接 """
        # 定义列表存储每本书详情链接
        print(page_url)
        book_url_list = []
        response = requests.get(page_url, headers=self.headers)
        pq_parse = PyQuery(response.text)
        li_list = pq_parse('.summary-list > .item').items()
        for li in li_list:
            href = 'https://read.douban.com' + li('.title > a').attr('href')
            title = li('.title > a').attr('title')
            book_url_list.append((title, href))
        return book_url_list

    def get_book_data(self, book_tuple):
        booK_title = book_tuple[0]  # 书籍标题
        book_url = book_tuple[1]  # 书籍详情页链接
        response = requests.get(book_url, headers=self.headers)
        pq_parse = PyQuery(response.text)('article-meta')
        author = pq_parse('p:nth-child(1) > span:nth-child(2) > a').text()  # 书籍作者
        book_type = pq_parse('p:nth-child(2) > span:nth-child(2)').text()  # 书籍类别
        publish = pq_parse('p:nth-child(3) > span:nth-child(2) > span:nth-child(1)').text()  # 出版社
        publish_time = datetime.strptime(pq_parse('p:nth-child(3) > span:nth-child(2) > span:nth-child(2)').text(),
                                         '%Y-%m-%d')  # 出版时间
        provider = pq_parse('p:nth-child(4) > span:nth-child(2) > a').text()  # 提供方
        size_num = pq_parse('p:nth-child(5) > span:nth-child(2)').text()  # 字数
        isbn = pq_parse('p:nth-child(6) > span:nth-child(2) > a').text()  # isbn
        data = {
            'book_title': booK_title,
            'author': author,
            'book_type': book_type,
            'publish': publish,
            'publish_time': publish_time,
            'provider': provider,
            'size_num': size_num,
            'isbn': isbn
        }
        return data

    def run(self):
        publish_tuple_list = self.get_publish_url()
        print(publish_tuple_list)
        for publish_tuple in publish_tuple_list:
            page_url_list = self.get_page_url(publish_tuple)
            print(page_url_list)
            for page_url in page_url_list:
                book_url_list = self.get_book_url(page_url)
                print(book_url_list)
                data_list = []
                for book_tuple in book_url_list:
                    data = self.get_book_data(book_tuple)
                    data_list.append(data)
                self.mongo.insert_many(data_list)
                time.sleep(0.5)


if __name__ == '__main__':
    spider = DouBanReadPublish()
    spider.run()
