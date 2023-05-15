"""
    采集虎牙美女主播封面图
        爬虫第一步: 寻找到目标数据源
        爬虫第二步: 与虎牙网站建立连接获取页面源码
        爬虫第三步: 从页面源码中解析出封面图src链接
        爬虫第四步: 对图片src链接发请求获取图片资源
"""
import re

import requests
from fake_useragent import UserAgent

url = 'https://www.huya.com/g/4079?page=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

source = requests.get(url, headers=headers).content.decode('utf-8')

regex = '<li class="game-live-item".*?class="pic" data-original="(.*?)".*?title="(.*?)的直播">.*?<p class="tag-right">'

pattern = re.compile(regex, re.S)

pic_url_lic = pattern.findall(source)
print(pic_url_lic)
for pic in pic_url_lic:
    print(pic[0].split('?')[0])
    pic_source = requests.get(pic[0].split('?')[0], headers=headers)
    with open('./虎牙美女主播/{}.jpg'.format(pic[1]), 'wb') as file:
        file.write(pic_source.content)
