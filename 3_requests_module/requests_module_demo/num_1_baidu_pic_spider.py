"""
    requests模块爬虫练习一 ==> 互联网图片抓取
    说明:
        图片, 音频, 视频再计算机中均以二进制方式存储
    功能实现:
        1. 找到要抓取图片的url地址
        2. 向图片url地址发送请求, 获取二进制响应内容(bytes)
        3. 将响应内容以wb的方式存入本地
    实现代码:
        html = requests.get(url=url, headers=headers)
        响应对象属性:
            1. 获取响应对象字符串内容: res.text
            2. 获取响应对象内容-bytes: res.content
            3. 获取HTTP响应码: res.status_code
            4. 返回实际数据url地址: res.url
"""
import json
import re
import time

import requests, os
from urllib import parse


class BaiDuPic:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9103933915177681016&ipn=rj&ct=201326592&is=&fp=result&fr=&word={}&queryWord={}&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&rn=30&gsm=1e&1642782190468='
        self.header = {
            # accept破解百度安全验证
            'Accept': 'text/plain, */*; q=0.01',
            "Referer": "https://image.baidu.com/search/index?",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    def get_html(self, url):
        res = requests.get(url, headers=self.header)
        return res

    def parse_re(self, html):
        # try:
        #     html = html.json()
        #     print(html['data'])
        #     print(len(html['data']))
        #     r_list = []
        #     for data in range(len(html['data']) - 1):
        #         link = html['data'][data]['thumbURL']
        #         name = html['data'][data]['fromPageTitleEnc']
        #         r_list.append((link, name))
        #     return r_list
        # except:
        html = html.text
        r_list = []
        regex = '"thumbURL":"(.*?)".*?"fromPageTitleEnc":"(.*?)"'
        pattern = re.compile(regex, re.S)
        for data in pattern.findall(html):
            r_list.append((data[0], data[1]))
        return r_list

    # def parse_re_zero(self, html):
    #     regex = '"thumbURL":"(.*?)".*?"fromPageTitleEnc":"(.*?)"'
    #     pattern = re.compile(regex, re.S)
    #     r_list = pattern.findall(html)
    #     return r_list

    def dowaload(self, i, j, url, name, word):
        res = self.get_html(url)
        pic_data = res.content
        with open('./{}/{}_{}_{}.jpg'.format(word, i, j, name), 'wb') as file:
            file.write(pic_data)

    def run(self):
        start = time.time()
        word = input('请输入您要下载的图片关键字:')
        num_pic = int(input('请输入您要下载的页数:'))
        try:
            os.mkdir('./{}'.format(word))
        except:
            print('文件夹已存在！！')
        result = parse.quote(word)
        for i in range(0, num_pic):
            # if i != 0:
            url = self.url.format(result, result, i * 30)
            res = self.get_html(url)
            # 数据解析获取图片链接
            list = self.parse_re(res)
            print(list)
            print(len(list))
            for j in range(len(list)):
                link = list[j]
                self.dowaload(i, j + 1, link[0].strip(),
                              link[1].strip().replace('\\', '_').replace('?', '_').replace('|', '_').replace('/', '_')
                              .replace(':', '_').replace('*', 'x').replace('"', '_').replace('>', '_').replace('<', '_')
                              .replace('\n', '_').replace(';', '_').replace(',', '_').replace('~', '_').replace('!',
                                                                                                                '_')
                              .replace('@', '_').replace('#', '_').replace('$', '_').replace('%', '_').replace('^', '_')
                              .replace('&', '_').replace('ǖ', '_').replace('\x08', '_').replace('\x01', '_').replace(
                                  '\x02', '_')
                              .replace('\x03', '_').replace('\x04', '_').replace('\x05', '_').replace('\x06',
                                                                                                      '_').replace(
                                  '\x07', '_').replace('\x09', '_').replace('\x10', '_').replace('\x00', '_'),
                              word)
            # else:
            #     url = 'https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word={}'.format(result)
            #     url = self.url.format(result, result, i * 30)
            #     res = self.get_html(url)
            #     # 数据解析获取图片链接
            #     list = self.parse_re_zero(res.text)
            #     print(list)
            #     for j in range(len(list)):
            #         link = list[j]
            #         self.dowaload(i, j + 1, link[0].strip(),
            #                       link[1].strip().replace('\\', '_').replace('?', '_').replace('|', '_').replace('/','_')
            #                       .replace(':', '_').replace('*', 'x').replace('"', '_').replace('>', '_').replace('<', '_')
            #                       .replace('\n', '_'),
            #                       word)
            print('第{}页图片下载完毕'.format(i + 1))
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    spider = BaiDuPic()
    spider.run()
