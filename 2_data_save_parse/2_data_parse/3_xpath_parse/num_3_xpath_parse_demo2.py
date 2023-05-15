"""
    xpath解析实战二 ==> 下载彼岸图网图片
"""

import time
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 创建文件夹存储图片
    try:
        os.mkdir('./xpath_pic实战')
    except:
        print('文件夹已存在')
    flag = True
    i = 1
    while True:
        # if判断是否为第一页
        if i == 1:
            url = 'https://pic.netbian.com/4kmeinv/index.html'
        else:
            url = 'https://pic.netbian.com/4kmeinv/index_{}.html'.format(i)

        # 发请求获取响应源码
        page = requests.get(url=url)
        page.encoding = 'gbk'
        # 实例化etree对象
        tree = etree.HTML(page.text)
        a_list = tree.xpath('//*[@id="main"]/div[3]/ul//a[@target="_blank"]')
        print(a_list)
        for a_pic in a_list:
            pic_link = 'https://pic.netbian.com' + a_pic.xpath('./@href')[0]
            # 发请求获取图片详情页源码
            pic_html = requests.get(pic_link)
            pic_html.encoding = 'gbk'
            # 实例化etree对象
            pic_tree = etree.HTML(pic_html.text)
            # 获取图片标题
            name = pic_tree.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()')[0].strip()
            # 获取图片链接
            pic_url = 'https://pic.netbian.com' + pic_tree.xpath('//*[@id="img"]/img/@src')[0]
            print(name, pic_url)
            # 请求获取图片内容
            content = requests.get(pic_url).content
            # 存储下载图片
            with open('./xpath_pic实战/{}.{}'.format(name, pic_url.split('.')[-1]), 'wb') as file:
                file.write(content)
        print('第{}页图片下载完毕！！'.format(i))
        time.sleep(1)
        i += 1
        if '下一页' not in page.text:
            flag = False
        else:
            pass
