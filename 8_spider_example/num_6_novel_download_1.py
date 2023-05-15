"""
    奇书网小说下载
"""
import random
import time

import requests
from lxml import etree
import os
import json
from threading import Thread
import multiprocessing


def book_down(url, headers, path, book_name):
    try:
        book_source = requests.get(url, headers=headers)
        book_source.encoding = 'GB2312'
        with open(path + '/{}.txt'.format(book_name), 'wb') as file:
            file.write(book_source.content)
    except:
        book_down(url, headers, path, book_name)


def img_down(url, headers, path, book_name):
    try:
        book_source = requests.get(url, headers=headers)
        book_source.encoding = 'GB2312'
        with open(path + '/{}.jpg'.format(book_name), 'wb') as file:
            file.write(book_source.content)
    except:
        img_down(url, headers, path, book_name)


def save_json(book_read_tree, path, book_name):
    data = {}
    data['书名'] = book_read_tree.xpath('/html/body/div/div[5]/div[1]/h1/text()')[0]
    data['作者'] = book_read_tree.xpath('/html/body/div/div[5]/div[1]/p[1]/text()')[0].split('：')[-1]
    data['分类'] = book_read_tree.xpath('/html/body/div/div[5]/div[1]/p[2]/text()')[0].split('：')[-1]
    data['大小'] = book_read_tree.xpath('/html/body/div/div[5]/div[1]/p[3]/span/text()')[0]
    data['内容简介'] = book_read_tree.xpath('/html/body/div/div[5]/div[2]/div[2]//text()')
    with open(path + '/{}.json'.format(book_name), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


def book_paese(book, book_type_name, headers):
    try:
        book_data_link = 'http://www.qishu.me' + book.xpath('./div[1]/span/a/@href')[0]
        print(book_data_link)
        # 请求获取每本书籍详情页面源码
        book_source = requests.get(book_data_link, headers=headers, timeout=2)
        book_source.encoding = 'GB2312'
        # 实例化etree对象
        book_tree = etree.HTML(book_source.text)
        # 解析书籍阅读页面链接
        book_read = book_tree.xpath('//*[@id="downAddress"]/a[3]/@href')[0]
        # 解析书籍下载链接
        book_download = book_tree.xpath('//*[@id="downAddress"]/a[2]/@href')[0]
        # 解析书籍名称
        book_name = book_tree.xpath('//*[@id="downAddress"]/a[2]/@href')[0].split('/')[-1].split('.')[0]
        # 为每本书创建文件夹保存
        path = './奇书网小说下载/{}/{}'.format(book_type_name, book_name)
        try:
            os.mkdir(path)
        except:
            pass
        # 调用函数下载小说
        book_down(book_download, headers, path, book_name)
        # 获取书籍阅读页面源码
        book_source_read = requests.get(book_read, headers=headers, timeout=2)
        # 实例化etree对象
        book_read_tree = etree.HTML(book_source_read.text)
        # 解析书籍封面链接
        img_url = book_read_tree.xpath('/html/body/div/div[5]/div[1]/div/img/@src')[0]
        # 调用函数下载封面
        img_down(img_url, headers, path, book_name)
        # 调用函数解析书籍简介保存json文件
        save_json(book_read_tree, path, book_name)
    except:
        book_paese(book, book_type_name, headers)


def book_type_down(book_type_name, book_type_keyword_name, book_type_keyword_num, headers):
    try:
        # 为每种类型数据建立文件夹保存
        try:
            os.mkdir('./奇书网小说下载/{}'.format(book_type_name))
        except:
            pass
        for i in range(1, 11):
            book_type_link = 'http://www.qishu.me/{}/{}_{}.html'.format(book_type_keyword_name, book_type_keyword_num,
                                                                        i)
            print(book_type_link)
            # 获取每种类别小说对应页面源码
            book_type_source = requests.get(book_type_link, headers=headers)
            book_type_source.encoding = 'GB2312'
            # 实例化etree对象
            book_type_tree = etree.HTML(book_type_source.text)
            # 获取每本小说详情与下载页面链接列表
            book_list = book_type_tree.xpath('//*[@id="listbox"]/div[@class="mainListInfo"]')
            print(len(book_list))
            for book in book_list:
                book_paese(book, book_type_name, headers)
            time.sleep(random.randint(0, 2))
    except:
        book_type_down(book_type_name, book_type_keyword_name, book_type_keyword_num, headers)


try:
    os.mkdir('./奇书网小说下载')
except:
    pass
# 起始url
start_url = 'http://www.qishu.me/'
# 定义请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'UM_distinctid=17ef85c36042ae-00ea7fec4d6dfb-f791539-144000-17ef85c3605d01; CNZZDATA1261416950=1003146946-1644839868-null%7C1644839868; __gads=ID=8b54018ef179b954-220a292b9ed00029:T=1644844330:RT=1644844330:S=ALNI_Mbo1C-A9AfUOvlhQ8ROh5yqTnWamA; CNZZDATA1835761=cnzz_eid%3D125164515-1644838904-null%26ntime%3D1644838904; Hm_lvt_0b955fc6fbfeb4990aa7b8d5c8d944aa=1644844303,1644844552; Hm_lpvt_0b955fc6fbfeb4990aa7b8d5c8d944aa=1644844552',
    # 'Host': 'www.qishu.me',
    # 'If-Modified-Since': 'Mon, 14 Feb 2022 02:27:31 GMT',
    # 'Referer': 'http://www.qishu.cc/',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
# 获取起始页源码
start_source = requests.get(start_url, headers=headers)
start_source.encoding = 'GB2312'
# print(start_source.text)
# 实例化etree对象
start_tree = etree.HTML(start_source.text)
type_list = start_tree.xpath('//*[@id="globalNavUL"]/li')[1:]
print(type_list)
for book_type in type_list:
    book_type_keyword_name = book_type.xpath('./a/@href')[0].split('/')[1]
    book_type_keyword_num = book_type.xpath('./a/@href')[0].split('/')[2].split('_')[0]
    book_type_name = book_type.xpath('./a/text()')[0]
    print(book_type_name, book_type_keyword_name, book_type_keyword_num)
    t = multiprocessing.Process(target=book_type_down,
                                args=(book_type_name, book_type_keyword_name, book_type_keyword_num, headers,))
    t.start()
