"""
    表情包采集:
        1. 寻找目标数据源
            表情包链接存在网页源代码中
        2. 分析网页结构
            ul id="post_container" -> li class="post box row fixed-hight" ->
            div class="thumbnail" -> a -> img
        3. 建立连接, 解析数据
        4. 下载保存数据
    网页url:http://www.bbsnet.com/biaoqingbao
"""

import requests
from lxml import etree
import time
import os

file_dir = input('请输入要保存的文件夹名:')
try:
    os.mkdir('./{}'.format(file_dir))
except:
    print('文件夹已存在！！')

# 定义变量计算页数
i = 1
# 定义Boolean变量控制循环
flag = True
# 定义请求头避免被反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
keyword = input('请输入图片关键字拼音:')
while flag:
    if i == 1:
        url = 'http://www.bbsnet.com/{}'.format(keyword)
    else:
        url = 'http://www.bbsnet.com/{}/page/{}'.format(keyword, i)
    # 与网站建立链接获取响应数据
    source = requests.get(url=url, headers=headers).content.decode()
    # 实例化etree对象
    tree = etree.HTML(source)
    # 解析数据
    img_list = tree.xpath('//*[@id="post_container"]/li')
    for img in img_list:
        img_src = img.xpath('./div[1]/a/img/@src')[0]
        img_title = img.xpath('./div[1]/a/img/@alt')[0]
        img_type = img_src.split('.')[-1]
        print(img_title, img_src)
        # 请求下载表情包
        try:
            pic_source = requests.get(img_src, headers=headers).content
            with open('./{}/{}.{}'.format(file_dir, img_title, img_type), 'wb') as file:
                file.write(pic_source)
        except:
            pass
    print('第{}页数据抓取完毕'.format(i))
    # 控制数据抓取频率
    time.sleep(2)

    if '下一页' not in source:
        flag = False
    else:
        i += 1
