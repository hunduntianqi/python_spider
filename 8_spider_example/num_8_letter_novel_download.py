"""
    文学作品类小说下载
"""
import os
import time

import requests
import re
from pyquery import PyQuery
import json


class WenXueTextDownload:
    def __init__(self):
        # 创建文件夹保存数据
        try:
            os.mkdir('./文学作品')
        except:
            print('文件夹已存在！！')
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'www.mingzhuxiaoshuo.com',
            'Referer': 'http://www.mingzhuxiaoshuo.com/mingqing/List_242.Html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
        }

    def getTypeLink(self):
        ''' 解析所有书籍分类链接 '''
        url = 'http://www.mingzhuxiaoshuo.com/Index.Html'
        response = requests.get(url=url, headers=self.headers)
        response.encoding = 'gb2312'
        # print(response.text)
        # 定义正则表达式解析所有书籍分类链接
        regex = '┊  <a class=awhite12 href="(.*?)" target="_self">(.*?)</a>'
        pattern = re.compile(regex, re.S)
        type_list = []  # 定义列表存储数据分类链接
        for type_sign in pattern.findall(response.text):
            print(type_sign)
            type_list.append(type_sign)
        return type_list

    def getBookLink(self, type_sign):
        ''' 提取每种类型下每本书的详情链接 '''
        book_type = type_sign[1]
        try:
            os.mkdir('./文学作品/{}'.format(book_type))
        except:
            print('文件夹已存在！！')
        book_type_link = [type_sign[0]]
        # book_type_link = ['http://www.mingzhuxiaoshuo.com/waiguo/']
        flag = True
        book_list_link = []
        while flag:
            response = requests.get(url=book_type_link[0], headers=self.headers)
            # response = requests.get(url='http://www.mingzhuxiaoshuo.com/waiguo/', headers=self.headers)
            response.encoding = 'gb2312'
            regex = '<A HREF=(.*?)>下一页</A>'
            pattern = re.compile(regex)
            book_next_page = pattern.findall(response.text)
            # for book in book_next_page:
            #     print(book)
            if len(book_next_page) == 0:
                flag = False
            else:
                book_type_link[0] = 'http://www.mingzhuxiaoshuo.com' + book_next_page[0]
                print(book_type_link[0])
            book_regex = '<TD align=center><A class=atuhuang12 href="(.*?)" target=_blank title=(.*?)>.*?</a></TD>'
            pattern_book = re.compile(book_regex, re.S)
            for book_link in pattern_book.findall(response.text):
                book_list_link.append((book_link, book_type))
                print((book_link, book_type))
            time.sleep(2)
        return book_list_link

    def getBookHtml(self, book):
        ''' 解析获取书籍详情页HTML信息 '''
        book_type = book[1]
        book_link = 'http://www.mingzhuxiaoshuo.com' + book[0][0]
        book_name = book[0][1]
        get_html = requests.get(book_link, headers=self.headers)
        get_html.encoding = 'gb2312'
        pq = PyQuery(get_html.text)
        author = pq('tr > td > div:nth-child(1)').text().split('|')[1].split("：")[1].strip()
        # 实例化PyQuery对象
        data = {}
        data['书名'] = book_name
        data['作者'] = author
        data['分类'] = book_type
        data['详情链接'] = book_link
        data['内容简介'] = pq('.hui14').text()
        img_regex = '<TD vAlign=top width=100><img src="(.*?)".*?height="125" width="100"/></TD></TR>'
        img_src = re.compile(img_regex, re.S).findall(get_html.text)[0]
        text_regex = 'href="/Down.asp?(.*?)"><font color="#FFFFFF">全本txt下载</font></A>'
        text_url = 'http://www.mingzhuxiaoshuo.com/Down.asp' + re.compile(text_regex, re.S).findall(get_html.text)[0]
        return [data, img_src, text_url]

    def downFile(self, book_list):
        ''' 下载文件 '''
        data = book_list[0]
        img_src = book_list[1]
        text_url = book_list[2]
        book_type = data['分类']
        book_name = data['书名']
        # 创建文件夹保存书籍文件
        try:
            os.mkdir('./文学作品/{}/{}'.format(book_type, book_name))
        except:
            print('文件夹已存在！！')
        # 保存json文件
        with open('./文学作品/{}/{}/{}.json'.format(book_type, book_name, book_name), 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        # 下载图片
        img_response = requests.get(img_src, headers=self.headers)
        with open('./文学作品/{}/{}/{}.jpg'.format(book_type, book_name, book_name), 'wb') as file:
            file.write(img_response.content)
        # 下载txt文件
        text_response = requests.get(text_url, headers=self.headers)
        with open('./文学作品/{}/{}/{}.txt'.format(book_type, book_name, book_name), 'wb') as file:
            file.write(text_response.content)
        # if os.path.getsize('./文学作品/{}/{}/{}.txt'.format(book_type, book_name, book_name)) <= 100:
        #     print('书籍{}下载失败')
        #     list_dir = os.listdir('./文学作品/{}/{}'.format(book_type, book_name))
        #     print(list_dir)
        #     for file_path in list_dir:
        #         os.remove('./文学作品/{}/{}/'.format(book_type, book_name) + file_path)
        #     os.remove('./文学作品/{}/{}'.format(book_type, book_name))

    def run(self):
        type_list = self.getTypeLink()
        for type_sign in type_list:
            print(type_sign)
            book_list_link = self.getBookLink(type_sign)
            print(book_list_link)
            for book in book_list_link:
                book_list = self.getBookHtml(book)
                print(book_list)
                self.downFile(book_list)
                # time.sleep(1)


if __name__ == '__main__':
    spider = WenXueTextDownload()
    spider.run()
