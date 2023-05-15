"""
    全面屏壁纸抓取
"""
import os
import time
from pyquery import PyQuery
import requests
from urllib import parse

try:
    os.mkdir('./images')
except:
    print('文件夹已存在！！')

key = input('请输入图片标签:')
# 图片类型编码
result = parse.quote(key)
# 构造请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
start_url = 'https://m.bcoderss.com/tag/{}/'.format(result)
num = 1
flag = True
while flag:
    if num == 1:
        url = start_url
        response = requests.get(url, headers=headers)
    else:
        url = 'https://m.bcoderss.com/tag/{}/page/{}/'.format(result, num)
        response = requests.post(url, headers=headers)
    # print(response.text)
    # 加载PyQuery对象
    pq = PyQuery(response.text)
    # 根据类名提取图片标签
    img_it = pq('.wp-post-image').items()
    for img in img_it:
        img_src = img.attr('src')
        img_name = img.attr('alt') + img_src.split('/')[-1]
        print(img_name, img_src)
        img_res = requests.get(img_src, headers=headers)
        with open('./images/{}'.format(img_name), 'wb') as file:
            file.write(img_res.content)
        time.sleep(0.5)
    if '加载更多' not in response.text:
        flag = False
    else:
        num += 1
    time.sleep(2)
