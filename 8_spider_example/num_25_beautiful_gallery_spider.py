"""
    优美图库图片抓取
"""

import requests
from bs4 import BeautifulSoup
import os


# param = {
#
# }
def pic_umei(header, proxies):
    num = 1
    while True:
        if num == 1:
            url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/index.htm'
        else:
            url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/index_{}.htm'.format(num)
        num += 1
        res = requests.get(url, headers=header, proxies=proxies)
        res.encoding = 'utf-8'
        # print(type(res.text))
        # break
        if res.text == '':
            break
        resp = BeautifulSoup(res.text, '2022-1-12-html.parser')
        li_data = resp.find(class_="TypeList").find('ul').find_all('li')
        for li_list in li_data:
            li_link = 'https://www.umei.cc' + li_list.find('a')['href']
            li_name = li_list.find('a').find('span').text
            img_url = li_list.find('a').find('img')['src']
            img_data = requests.get(img_url, headers=header, proxies=proxies).content
            try:
                os.mkdir('./优美Pic/{}'.format(li_name))
            except:
                print('文件夹{}已存在！！'.format(li_name))
            img_file = open('./优美Pic/{}/{}.jpg'.format(li_name, li_name), 'wb')
            img_file.write(img_data)
            img_file.close()
            pic_num = 1
            while True:
                if pic_num == 1:
                    pic_url = li_link
                else:
                    pic_url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/236437_{}.htm'.format(pic_num)
                pic_num += 1
                pic_res = requests.get(pic_url, headers=header, proxies=proxies)
                if pic_res.text == '':
                    break
                pic_res.encoding = 'utf-8'
                pic_resp = BeautifulSoup(pic_res.text, '2022-1-12-html.parser')
                pic_img_src = pic_resp.find(class_="ImageBody").find('img')['src']
                pic_img_src_res = requests.get(pic_img_src, headers=header, proxies=proxies).content
                with open('./优美Pic/{}/{}_{}.jpg'.format(li_name, li_name, pic_num), 'wb') as pic_file:
                    pic_file.write(pic_img_src_res)
            print(li_name + '已下载完毕！！！')
        break


if __name__ == '__main__':
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'referer': 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
    }
    # 创建代理IP
    proxies = {
        """
        'http':'http://代理IP地址',要请求的网站开头为http
        'https':'https://代理IP地址'要请求的网站开头为https
        """
        'https': '106.45.104.227:3256'
    }
    pic_umei(header, proxies)
    print('全部下载完毕！！！')
