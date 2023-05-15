"""
    新浪微博图片抓取
"""

import time
import requests
import os


class WeiBoSpider(object):
    def __init__(self):
        try:
            self.fixname = input('请输入保存文件夹名称:')
            os.mkdir('./{}'.format(self.fixname))
        except:
            print('文件夹已存在！！')
        self.user_id = input('请输入微博用户id:')
        self.referer = 'https://weibo.com/u/{}'.format(self.user_id)
        self.url = 'https://weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0'
        # 'https://weibo.com/ajax/statuses/mymblog?uid=3276213840&page=1&feature=0'
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': self.referer,
            'cookie': 'SINAGLOBAL=3702733535934.266.1644503978470; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFT1ZCZUE3JQP4LZvaRwTKC5JpX5KMhUgL.Fo-E1KeEeoqpehM2dJLoIEBLxKqLBoMLBoMLxKqLBozL12eLxK-LBKBLBK.LxKML1hzL1h2t; UOR=,,www.baidu.com; ALF=1676203550; SSOLoginState=1644667551; SCF=AmDn3NT-atRSk3HwlKINB7cRH83b2fc-JEQ-z7UBzeAsdGELRzrpgVXleMWMkmNrSzPqOTFekPyCx0v_mW18WuI.; SUB=_2A25PA9LPDeRhGeNM4lET8ijNyzuIHXVseUMHrDV8PUNbmtB-LRbWkW9NSf56lXsSXKDMz6Re0mIQmFGtppGTpHMR; XSRF-TOKEN=qQGUM85MLc_g7YSSzKrTRTl1; WBPSESS=YSU4jOXnqmJtyrjIMtr4E3scPz8Lx8nC8CAkemxpvVxOQuKmkGUNMWAT1txlA-0T1rBbsP6Dg3vUZfl25yOSWNAupCs03Pzjf5bTCHqVmLHGFNnDg2MwYAavtJSMbc97-QuzXs3PfV_ViT8xMF0XNg==; _s_tentry=weibo.com; Apache=8688302506726.542.1644672464245; ULV=1644672464301:3:3:3:8688302506726.542.1644672464245:1644584428266',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        return response

    def parse_pic(self, response):
        url_list = []
        pic_data = response.json()['data']['list']
        for pic_sign in pic_data:
            print(pic_sign['text_raw'])
            name = pic_sign['text_raw'].strip().replace(':', '_').replace('/', '_').replace('\n', '_').replace(' ', '')
            try:
                os.mkdir('./{}/{}'.format(self.fixname, name))
            except:
                print('文件夹已存在！！')
            # print(pin_sign['pic_infos'])
            # print(pic_sign['pic_infos'].items())
            if 'pic_infos' in pic_sign.keys():
                pic_list = pic_sign['pic_infos']
                for key in pic_list:
                    # print(pic_sign['pic_infos'][key])
                    pic_url = pic_list[key]['largest']['url']
                    print(name, pic_url)
                    url_list.append((name, pic_url))
        return url_list

    def pic_down(self, url):
        pic_response = requests.get(url[1], headers=self.headers)
        content = pic_response.content
        name = url[1].split('.')[-2].split('/')[-1]
        type_pic = url[1].split('.')[-1]

        file = open('./{}/{}/{}.{}'.format(self.fixname, url[0], name, type_pic), 'wb')
        file.write(content)
        file.close()
        print(name)

    def run(self):
        page = int(input('请输入您要抓取的数据页数:'))
        for i in range(page):
            url = self.url.format(self.user_id, i + 1)
            # url = 'https://weibo.com/ajax/statuses/mymblog?uid=3276213840&page=1&feature=0'
            response = self.get_response(url)
            pic_list = self.parse_pic(response)
            for pic_url in pic_list:
                self.pic_down(pic_url)
            print('第{}页图片抓取完毕！！'.format(i + 1))
            time.sleep(2)


if __name__ == '__main__':
    spider = WeiBoSpider()
    spider.run()
