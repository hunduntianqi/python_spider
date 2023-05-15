"""
    回车桌面图片抓取
"""
import os, random
import time
from fake_useragent import UserAgent
from threading import Thread
import gevent
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests
import re

try:
    os.mkdir('./huichezhuomianimages')
except:
    print('文件夹已存在！！')

def img_download(dir_name, url, headers):
    img_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open('./huichezhuomianimages/{}/{}'.format(dir_name, img_name), 'wb') as file:
        file.write(response.content)

def get_img_list(url_tuple, headers):
    dir_name = url_tuple[1]
    try:
        os.mkdir('./huichezhuomianimages/{}'.format(dir_name))
    except:
        print('文件夹已存在！！')
    response = requests.get(url_tuple[0], headers=headers)
    regex = '<div class="swiper-slide">.*?src="(.*?)".*?title=.*?</a></div>'
    pattern = re.compile(regex, re.S)
    img_list = pattern.findall(response.text)
    print(img_list)
    for img_src in img_list:
        img_download(dir_name, img_src, headers)
    print('<<{}>>下载完成！！'.format(dir_name))



def get_img_data(work, headers):
    while not work.empty():
        url = work.get_nowait()
        # 请求获取响应数据
        response = requests.get(url, headers=headers)
        regex = '<dl class="egeli_pic_dl">.*?<a href="(.*?)" target="_blank"><img.*?title="(.*?)"/></a></dd>'
        pattern = re.compile(regex, re.S)
        link_list = pattern.findall(response.text)
        for link_tuple in link_list:
            get_img_list(link_tuple, headers)
            time.sleep(2)


# 请输入图片关键字(拼音)
img_key = input('请输入图片关键字(拼音):')
# 定义请求头
headers = {
    'referer': 'https://mm.enterdesk.com/qingchunmeinv/',
    'cookie': 't=817fdb5173608296d59fa4725e13423c; r=2810; Hm_lvt_86200d30c9967d7eda64933a74748bac=1646571726,1646580722; Hm_lpvt_86200d30c9967d7eda64933a74748bac=1646580722',
    'user-agent': str(UserAgent().random)
}
# 发送请求获取响应
url = 'https://mm.enterdesk.com/{}/1.html'.format(img_key)
response = requests.get(url, headers=headers)
print(response.text)
# 提取总页数
regex = '<li><a class="wrap no_a"  href="https://mm.enterdesk.com/{}/(.*?).html">末页</a></li>'.format(img_key)
pattern = re.compile(regex, re.S)
page_tatol = int(pattern.findall(response.text)[0])
print(page_tatol)
url_list = []
# 拼接所有页面url
for i in range(page_tatol):
    url = "https://mm.enterdesk.com/{}/{}.html".format(img_key, i + 1)
    url_list.append(url)
print(url_list)
work = Queue()
for url_img in url_list:
    work.put_nowait(url_img)

task_list = []
for i in range(len(url_list)):
    get_img_data(work, headers)
    # t = Thread(target=get_img_data, args=(work, headers, ))
    # t.start()
    # task = gevent.spawn(get_img_data, work=work, headers=headers)
    # task_list.append(task)
# gevent.joinall(task_list)