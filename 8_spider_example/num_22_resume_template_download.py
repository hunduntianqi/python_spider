"""
    免费简历模板下载
"""
import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
num = 49
while True:
    if num == 1:
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        url = 'https://sc.chinaz.com/jianli/free_{}.2022-1-12-html'.format(num)
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    jianli_link = tree.xpath('//*[@id="container"]/div')
    for jianli_list in jianli_link:
        # print(jianli_list)
        link = 'https:' + jianli_list.xpath('./p/a/@href')[0]
        name = jianli_list.xpath('./p/a/text()')[0].strip()
        res_data = requests.get(link, headers=header)
        jianli_data_link = etree.HTML(res_data.text).xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        jianli = requests.get(jianli_data_link, headers=header).content
        file = open('./简历模板/{}'.format(name), 'wb')
        file.write(jianli)
        file.close()
    print('第{}页简历模板已下载完毕！！'.format(num))
    if res.text == '':
        break
    else:
        num += 1