"""
    下厨房首页食谱信息抓取
"""

import requests
import os
from lxml import etree
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
num = 1
while True:
    os.mkdir('./菜谱/第{}页'.format(num))
    url = 'https://www.xiachufang.com/explore/?page={}'.format(num)

    res = requests.get(url, headers=header)
    resp = BeautifulSoup(res.text, '2022-1-12-html.parser')
    link_list = resp.find_all(class_="recipe recipe-215-horizontal pure-g image-link display-block")
    for link_href in link_list:
        link = 'https://www.xiachufang.com/' + link_href.find('a')['href']
        # print(link)
        link_res = requests.get(link, headers=header)
        link_resp = BeautifulSoup(link_res.text, '2022-1-12-html.parser')
        name = link_resp.find(class_="page-title").text.strip()
        material = link_resp.find(class_="block recipe-show").find('h2').text.strip()
        material_list = link_resp.find(class_="ings").find_all('tr')
        pic_link = link_resp.find(class_="cover image expandable block-negative-margin").find('img')['src']
        pic_data = requests.get(pic_link).content
        try:
            os.mkdir('./菜谱/第{}页/{}'.format(num, name))
            with open('./菜谱/第{}页/{}/{}.jpg'.format(num, name, name), 'wb') as pic:
                pic.write(pic_data)
            with open('./菜谱/第{}页/{}/用料.text'.format(num, name), 'w') as mate:
                mate.write(material + '\n')
                for mater in material_list:
                    mater_name = mater.find(class_="name").text.strip()
                    mater_quality = mater.find(class_="unit").text.strip()
                    mater_data = mater_name + ':' + mater_quality + '\n'
                    mate.write(mater_data)
            practice = link_resp.find(id="steps").text.strip()
            os.mkdir('./菜谱/第{}页/{}/{}'.format(num, name, practice))
            steps = link_resp.find(class_="steps").find('ol').find_all('li')
            for step in steps:
                pic_name1 = step.find('img')['alt'].strip()
                pic_name2 = step.find(class_="text").text.strip()
                pic_name = pic_name1 + '-' + pic_name2
                pic_data = requests.get(step.find('img')['src'], headers=header).content
                with open('./菜谱/第{}页/{}/{}/{}.jpg'.format(num, name, practice, pic_name), 'wb') as file:
                    file.write(pic_data)
            print('{}做法已下载完毕'.format(name))
        except:
            print('{}因名字不符规则无法创建文件夹'.format(name))
    num += 1
    if num == 21:
        break
