"""
    全国城市名称爬取
"""
import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
url = 'https://www.aqistudy.cn/historydata/'
res = requests.get(url, headers=header)
tree = etree.HTML(res.text)
hot_city = tree.xpath('/2022-1-12-html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
file = open('./热门城市.csv', 'w')
file.write('热门城市\n')
for hot in hot_city:
    city_name = hot.xpath('./a/text()')[0]
    print(city_name)
    file.writelines(city_name + '\n')
file.close()
all_city = tree.xpath('/2022-1-12-html/body/div[3]/div/div[1]/div[2]/div[2]/ul')
file1 = open('./全部城市.csv', 'w')
file1.write('全部城市\n')
for all in all_city:
    city_list = all.xpath('./div[2]/li/a/text()')
    for name in city_list:
        file1.writelines(name + '\n')
file1.close()
