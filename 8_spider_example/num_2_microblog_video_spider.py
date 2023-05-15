"""
    新浪微博视频抓取
"""

import time

import requests
import os
import re
import emoji


class WeiBoSpiderVideo(object):
    def __init__(self):
        try:
            self.fixname = input('请输入保存文件夹名称:')
            os.mkdir('./{}'.format(self.fixname))
        except:
            print('文件夹已存在！！')
        self.user_id = input('请输入微博用户id:')
        self.referer = 'https://weibo.com/u/{}'.format(self.user_id)
        self.url = 'https://weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0'
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'referer': self.referer,
            'cookie': 'SINAGLOBAL=3702733535934.266.1644503978470; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFT1ZCZUE3JQP4LZvaRwTKC5JpX5KMhUgL.Fo-E1KeEeoqpehM2dJLoIEBLxKqLBoMLBoMLxKqLBozL12eLxK-LBKBLBK.LxKML1hzL1h2t; UOR=,,www.baidu.com; ULV=1644584428266:2:2:2:4720834535133.092.1644584428260:1644503978497; WBPSESS=YSU4jOXnqmJtyrjIMtr4E3scPz8Lx8nC8CAkemxpvVxOQuKmkGUNMWAT1txlA-0T1rBbsP6Dg3vUZfl25yOSWGvQb_cM5o822_31B2o4YtLgCDOvDMvfo7vrJraHcK3Df1rnRE2FXxAVczizeQ7xVQ==; ALF=1676203550; SSOLoginState=1644667551; SCF=AmDn3NT-atRSk3HwlKINB7cRH83b2fc-JEQ-z7UBzeAsdGELRzrpgVXleMWMkmNrSzPqOTFekPyCx0v_mW18WuI.; SUB=_2A25PA9LPDeRhGeNM4lET8ijNyzuIHXVseUMHrDV8PUNbmtB-LRbWkW9NSf56lXsSXKDMz6Re0mIQmFGtppGTpHMR; XSRF-TOKEN=qQGUM85MLc_g7YSSzKrTRTl1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        return response

    def parse_video(self, response):
        url_list = []
        print(response.json())
        video_data = response.json()['data']['list']
        for video_sign in video_data:
            # print(video_sign['text_raw'])
            # print(pin_sign['video_infos'])
            # print(video_sign['video_infos'].items())
            if 'page_info' in video_sign.keys():
                try:
                    video_url= video_sign['page_info']['media_info']['playback_list'][-1]['play_info']['url']
                    video_name = video_sign['page_info']['media_info']['kol_title']
                    print(video_name, video_url)
                    url_list.append((video_name, video_url))
                except:
                    print('非视频图片！！')
        return url_list

    def video_down(self, url, video_name):
        video_response = requests.get(url, headers=self.headers)
        content = video_response.content
        try:
            name = video_name
            file = open('./{}/{}.mp4'.format(self.fixname, name), 'wb')
            file.write(content)
            file.close()
            print('{}视频下载完毕！！'.format(name))
        except:
            name = video_name.split()[0]
            file = open('./{}/{}.mp4'.format(self.fixname, name), 'wb')
            file.write(content)
            file.close()
            print('{}视频下载完毕！！'.format(name))

    def run(self):
        page = int(input('请输入您要抓取的数据页数:'))
        for i in range(5, page):
            url = self.url.format(self.user_id, i + 1)
            response = self.get_response(url)
            video_list = self.parse_video(response)
            for video_url in video_list:
                self.video_down(video_url[1], video_url[0])
            print('第{}页视频抓取完毕！！'.format(i + 1))
            time.sleep(2)


if __name__ == '__main__':
    spider = WeiBoSpiderVideo()
    spider.run()