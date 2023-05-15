"""
    bs4解析实战 ==> 彼岸美图4k图片爬取
"""
# 导入模块
import time
import os
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 创建文件夹存储下载的图片
try:
    os.mkdir('./images')
except:
    print('文件夹已存在！！')
# 第一页链接与其他页面链接不同, 先定义初始url地址
start_url = 'https://pic.netbian.com/4kmeinv/index.html'

# 定义请求头
herders = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__yjs_duid=1_54c6fc449e35d5f1f7e5882012983cb21680440769532; zkhanecookieclassrecord=%2C54%2C; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1680440765; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1680440789',
    'if-modified-since': 'Sat, 05 Feb 2022 17:38:14 GMT',
    'referer': 'https://pic.netbian.com/4kmeinv/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
}

i = 1  # 定义变量记录抓取页数
flag = True  # 定义变量记录循环条件, 判断循环是否终止
while flag:
    # if判断是否为第一页
    if i == 1:
        url = start_url
    else:
        url = 'https://pic.netbian.com/4kmeinv/index_{}.html'.format(i)
    # 获取页面所有图片源码信息
    response_source_text = requests.get(url=url)
    response_source_text.encoding = 'gbk'
    print(response_source_text.text)
    # 实例化Beautiful对象, 解析图片详情链接
    soup_source = BeautifulSoup(response_source_text.text, 'lxml')
    pic_link_list = soup_source.find('ul', class_="clearfix").find_all('a')
    for pic_link in pic_link_list:
        # 拼接图片详情链接
        pic_data = 'https://pic.netbian.com' + pic_link['href']
        print(pic_data)
        # 获取图片详情页面源码信息
        response_pic = requests.get(pic_data)
        response_pic.encoding = 'gbk'
        # 实例化beautiful对象解析图片大图链接
        soup_pic = BeautifulSoup(response_pic.text, 'lxml')
        pic_url = 'https://pic.netbian.com' + soup_pic.find(id="img").find('img')['src']
        pic_name = soup_pic.find('div', class_="photo-hd").text
        # 请求获取图片信息
        pic_source = requests.get(pic_url)
        content = pic_source.content
        # 保存图片
        with open('./images/{}.jpg'.format(pic_name), 'wb') as file:
            file.write(content)
        print(pic_name + '下载完毕')
    print('第{}页图片下载完毕！！'.format(i))
    time.sleep(1)
    i += 1
    # 判断是否为最后一页数据, 决定是否修改flag的值
    if '下一页' not in response_source_text.text:
        flag = False
    else:
        pass
