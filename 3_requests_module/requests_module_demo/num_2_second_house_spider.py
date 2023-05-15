"""
    requests模块爬虫练习二 ==> 抓取链家二手房网站中的房源信息
    抓取数据:
        房源名称, 地址, 户型, 面积, 方位, 是否精装, 楼层, 年代, 类型, 总价, 单价
"""
import csv
import time
import requests
from lxml import etree

city = input('请输入搜索城市拼音简写:')
num = int(input('请输入查询页数:'))
url = 'https://{}.lianjia.com/ershoufang/pg{}'
list = []
tuple_head = ('房源名称', '地址', '房源信息', '单价', '总房价(万)')
list.append(tuple_head)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Host': '{}.lianjia.com'.format(city),
    'Referer': 'https://{}.lianjia.com/ershoufang/'.format(city),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

for i in range(1, num + 1):
    for j in range(3):
        res_data = requests.get(url.format(city, i), headers=headers, timeout=3)
        tree = etree.HTML(res_data.text)
        data_list = tree.xpath('//*[@id="content"]/div[1]/ul/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        if len(data_list) == 0:
            break
        print(data_list)
        print(len(data_list))
        for data in data_list:
            name = data.xpath('./div[@class="info clear"]/div[@class="title"]/a/text()')[0].strip()
            address = data.xpath('./div[1]/div[2]/div/a[1]/text()')[0].strip() + '-' + \
                      data.xpath('./div[1]/div[2]/div/a[2]/text()')[0].strip()
            data_hourse = data.xpath('./div[1]/div[3]/div/text()')[0].strip().replace('|', '/')
            # print(data_hourse)
            price_hourse = data.xpath('./div[1]/div[6]/div[2]/span/text()')[0].strip()
            all_price = data.xpath('./div[1]/div[6]/div[1]/span/text()')[0].strip()
            hourse_tuple = (name, address, data_hourse, price_hourse, all_price)
            list.append(hourse_tuple)
            with open('./{}链家二手房房源信息.csv'.format(city), 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(list)
            list.clear()
        print('第{}页数据抓取完毕！！'.format(i))
        time.sleep(1)
        break
