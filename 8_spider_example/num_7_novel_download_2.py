"""
    久久小说下载网小说下载
"""
import requests
from lxml import etree
import os
import json
from threading import Thread


def bookSpider(book):
    book_link = 'https://www.txt909.com' + book.xpath('./a/@href')[0]
    book_name = book.xpath('./a/@title')[0]
    print(book_name, book_link)
    # 为每一本书创建文件夹保存
    try:
        os.mkdir('./小说下载/{}/{}'.format(book_type_title, book_name))
    except:
        print('文件夹已存在！！')
    # 向书籍详情页发送请求
    book_content = requests.get(book_link, headers=headers)
    # 实例化etree对象
    tree = etree.HTML(book_content.text)
    # 创建字典保存书籍简介信息
    book_introduct = {}
    book_introduct['书籍名称'] = book_name
    book_introduct['书籍作者'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[1]/a/text()')[0]
    book_introduct['书籍分类'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[2]/text()')[0]
    book_introduct['书籍大小'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[3]/text()')[0]
    book_introduct['内容简介'] = tree.xpath('//*[@id="mainSoftIntro"]//text()')
    print(book_introduct)
    with open('./小说下载/{}/{}/{}.json'.format(book_type_title, book_name, book_name), 'w', encoding='utf-8') as file:
        json.dump(book_introduct, file, ensure_ascii=False)
    book_img_link = tree.xpath('//*[@id="downInfoArea"]/div[3]/span/img/@src')[0]
    # 请求获取图片内容
    img_source = requests.get(book_img_link, headers=headers)
    with open('./小说下载/{}/{}/{}.jpg'.format(book_type_title, book_name, book_name), 'wb') as file:
        file.write(img_source.content)
    # 获取书籍下载页面链接
    book_down_link = tree.xpath('//*[@id="mainstory"]/ul[1]/li[1]/a/@href')[0]
    book_homepage_source = requests.get(book_down_link, headers=headers)
    # 实例化etree对象
    book_down_tree = etree.HTML(book_homepage_source.text)
    # 解析数据下载链接
    book_download_link = book_down_tree.xpath('//*[@id="info"]/p[6]/a/@href')[0]
    # 下载书籍
    book_download = requests.get(book_download_link, headers=headers)
    with open('./小说下载/{}/{}/{}.txt'.format(book_type_title, book_name, book_name), 'wb') as file:
        file.write(book_download.content)


try:
    os.mkdir('./小说下载')
except:
    print('文件夹已存在！！')

# 起始页url
start_url = 'https://www.txt909.com/'
# 请求头
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'UM_distinctid=17ef3038d3842e-0a7b29450aa402-f791539-144000-17ef3038d39dcd; CNZZDATA1276359776=1276106228-1644747562-https%253A%252F%252Fwww.so.com%252F%7C1644747562; articlevisited=1',
    'referer': 'https://www.txt909.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
# 起始页源码数据获取
start_source = requests.get(start_url, headers=headers)
# print(start_source.text)
# etree对象实例化
start_tree = etree.HTML(start_source.text)
book_type_list = start_tree.xpath('//*[@id="navber"]/div/ul/li')[1:]
for book_type in book_type_list:
    print(book_type)
    # 解析书籍各分类详情链接
    book_type_link = 'https://www.txt909.com' + book_type.xpath('./a/@href')[0]
    book_type_title = book_type.xpath('./a/@title')[0]
    print(book_type_title, book_type_link)
    # 为每种书籍分类建立文件夹
    try:
        os.mkdir('./小说下载/{}'.format(book_type_title))
    except:
        print('文件夹已存在！！')
    # 对每种书籍第一页发送请求
    book_source = requests.get(book_type_link, headers=headers)
    # 实例化etree对象
    book_tree = etree.HTML(book_source.text)
    # 解析获取每一本书籍链接
    book_list = book_tree.xpath('//*[@id="catalog"]/div')
    for book in book_list:
        t = Thread(target=bookSpider, kwargs={'book': book})
        t.start()
        # bookSpider(book)
        # book_link = 'https://www.txt909.com' + book.xpath('./a/@href')[0]
        # book_name = book.xpath('./a/@title')[0]
        # print(book_name, book_link)
        # # 为每一本书创建文件夹保存
        # try:
        #     os.mkdir('./小说下载/{}/{}'.format(book_type_title, book_name))
        # except:
        #     print('文件夹已存在！！')
        # # 向书籍详情页发送请求
        # book_content = requests.get(book_link, headers=headers)
        # # 实例化etree对象
        # tree = etree.HTML(book_content.text)
        # # 创建字典保存书籍简介信息
        # book_introduct = {}
        # book_introduct['书籍名称'] = book_name
        # book_introduct['书籍作者'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[1]/a/text()')[0]
        # book_introduct['书籍分类'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[2]/text()')[0]
        # book_introduct['书籍大小'] = tree.xpath('//*[@id="downInfoArea"]/div[3]/li[3]/text()')[0]
        # book_introduct['内容简介'] = tree.xpath('//*[@id="mainSoftIntro"]//text()')
        # print(book_introduct)
        # with open('./小说下载/{}/{}/{}.json'.format(book_type_title, book_name, book_name), 'w', encoding='utf-8') as file:
        #     json.dump(book_introduct, file, ensure_ascii=False)
        # book_img_link = tree.xpath('//*[@id="downInfoArea"]/div[3]/span/img/@src')[0]
        # # 请求获取图片内容
        # img_source = requests.get(book_img_link, headers=headers)
        # with open('./小说下载/{}/{}/{}.jpg'.format(book_type_title, book_name, book_name), 'wb') as file:
        #     file.write(img_source.content)
        # # 获取书籍下载页面链接
        # book_down_link = tree.xpath('//*[@id="mainstory"]/ul[1]/li[1]/a/@href')[0]
        # book_homepage_source = requests.get(book_down_link, headers=headers)
        # # 实例化etree对象
        # book_down_tree = etree.HTML(book_homepage_source.text)
        # # 解析数据下载链接
        # book_download_link = book_down_tree.xpath('//*[@id="info"]/p[6]/a/@href')[0]
        # # 下载书籍
        # book_download = requests.get(book_download_link, headers=headers)
        # with open('./小说下载/{}/{}/{}.txt'.format(book_type_title, book_name, book_name), 'wb') as file:
        #     file.write(book_download.content)
