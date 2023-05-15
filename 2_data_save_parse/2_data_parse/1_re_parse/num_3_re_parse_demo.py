"""
    re解析实战 ==> 抓取猫眼电影TOP100的电影名称, 主演, 上映时间信息
"""
import random
import re
import time
from urllib import request


class MaoYanSpider:
    def __init__(self):
        """定义参数"""
        self.url = 'https://www.maoyan.com/board/4?timeStamp=1680439237839&channelId=40011&index=4&signKey=4e2ea2656ace54ff05f9773bd506ea61&sVersion=1&webdriver=false&offset={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
            'Referer': 'https://www.maoyan.com',
            'Cookie': '__mta=142398989.1680439214390.1680439321775.1680439326537.11; uuid_n_v=v1; uuid=86D68590D15311ED9B401DCFC38BBF87FEEFB52CC5B74E4387EB630B4E66C853; _csrf=b71be1e82f9324ea7d1454eb65e36323f65800d59ec8c9902443f0388d9bb117; _lxsdk_cuid=18741fb808fc8-0d62d941984362-7868796f-1fa400-18741fb808fc8; _lxsdk=86D68590D15311ED9B401DCFC38BBF87FEEFB52CC5B74E4387EB630B4E66C853; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1680439214; __mta=142398989.1680439214390.1680439232607.1680439233961.5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1680439326; _lxsdk_s=18741fb8090-ad5-856-d39%7C%7C22'
        }

    def get_html(self, url):
        """获取响应内容"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # print(html)
        print(res.geturl())
        return html

    def parse(self, html):
        """数据解析函数"""
        # 定义正则匹配规则
        regex = '<div class="board-item-content">.*?title="(.*?)" data-act="boarditem-click".*?<p class="star">' \
                '(.*?)</p>.*?上映时间：(.*?)</p>    </div>'
        pattern = re.compile(regex, re.S)
        # r_list = [(name, star, time), (), ()....]
        r_list = pattern.findall(html)
        print(r_list)
        return r_list

    def save_html(self, r_list):
        """数据处理函数"""
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 10):
            url = self.url.format(offset * 10)
            html = self.get_html(url)
            r_list = self.parse(html)
            self.save_html(r_list)
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    maoyan = MaoYanSpider()
    maoyan.run()
