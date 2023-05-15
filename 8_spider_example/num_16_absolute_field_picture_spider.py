"""
    绝对领域图片抓取
"""
import os
import gevent
from gevent import monkey

# 使程序进入异步执行环境
monkey.patch_all()

from gevent.queue import Queue
import requests
from lxml import etree

# 创建文件夹存储图片
try:
    os.mkdir('./images')
except:
    print('文件夹已存在！！')


def download_img(img_url, img_name, type_name):
    try:
        res_img = requests.get(img_url, headers)
        with open('./images/{}.{}'.format(img_name, type_name), 'wb') as file:
            file.write(res_img.content)
        return
    except:
        download_img(img_url, img_name, type_name)


def image_parse(url, headers):
    print(url)
    # 获取页面源码
    response = requests.get(url, headers)
    # 实例化etree对象
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//*[@id="post-list"]/ul/li')
    for li in li_list:
        img_link = li.xpath('./div/div[1]/a/picture/img/@src')[0]
        img_name = li.xpath('./div/div[1]/a/picture/img/@alt')[0]
        type_name = img_link.split('.')[-1]
        download_img(img_link, img_name, type_name)


def tag_pic(work, headers):
    while not work.empty():
        url = work.get_nowait()
        # 请求获取每个标签下的页面源码
        response_tag = requests.get(url, headers=headers)
        # print(response_tag.text)
        # 实例化etree对象
        tree = etree.HTML(response_tag.text)
        max_page = int(tree.xpath('//*[@id="primary-home"]/div[2]/@data-max')[0])
        for i in range(1, max_page + 1):
            if i == 1:
                url_pic = url
                image_parse(url_pic, headers)
            else:
                url_pic = url + '/page/{}'.format(i)
                image_parse(url_pic, headers)


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'UM_distinctid=17f5838a4bd8b7-0ccd294e8c146c-977173c-144000-17f5838a4bec7d; CNZZDATA1259270526=1611192306-1646446694-https%253A%252F%252Fwww.baidu.com%252F%7C1646534650; Hm_lvt_2ae74021fe55d754e2dba2ce56ff1a11=1646452585,1646536731; Hm_lpvt_2ae74021fe55d754e2dba2ce56ff1a11=1646537320',
    'referer': 'https://www.jdlingyu.com/tuji',
    'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
url = 'https://www.jdlingyu.com/tags'
response = requests.get(url, headers=headers)
# print(response.text)
# 实例化etree对象
tree = etree.HTML(response.text)
url_start_list = []
li_list = tree.xpath('//*[@id="main"]/ul/li')
for url_li in li_list:
    url_link = url_li.xpath('./a/@href')[0]
    url_start_list.append(url_link)
print(len(url_start_list))
work_tag = Queue()
for url in url_start_list:
    # 将url添加到队列中
    work_tag.put_nowait(url)
task_list = []
for num in range(len(url_start_list)):
    t = gevent.spawn(tag_pic, work_tag, headers)
    task_list.append(t)
gevent.joinall(task_list)
