"""
    王者皮肤采集
        1. https://pvp.qq.com/web201605/herolist.shtml: 获取每个英雄详情链接
        2. 在每个英雄详情链接中获取默认背景皮肤链接和所有皮肤名称
        3. 使用字符串切割方式或取英雄皮肤数量
        4. 使用for循环拼接每个英雄皮肤的图片链接
        5. 下载保存英雄皮肤
"""
import time

import requests
import re
import os

# 定义初始url , 获取每个英雄的详情链接
start_url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'pgv_pvid=2154537165; LW_uid=f1x654T4i0m731T1p5G905P014; eas_sid=x1J6x4T4u0w701a1B5r9G5A3z4; PTTosSysFirstTime=1644019200000; PTTuserFirstTime=1644019200000; PTTosFirstTime=1644019200000; ts_refer=www.baidu.com/link; ts_uid=9248576872; pgv_pvi=7796365312; LW_sid=C1L6w45467W3F5y4k4o9t4E6s6; eas_entry=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2TdLsN6hjFhkgZrn6yqn2kCbkezDrocrmGrC__42CIm%26wd%3D%26eqid%3Dbb7f79f6002110d3000000036208abdb; isHostDate=19036; isOsSysDate=19036; isOsDate=19036; pgv_info=ssid=s8949936772; weekloop=0-6-0-8; ieg_ingame_userid=sgrOHczfXkd3vFDjjAb4uVMfI6Eh63eB; ts_last=pvp.qq.com/web201605/herodetail/542.shtml; pvpqqcomrouteLine=index_herolist_herodetail_herodetail; PTTDate=1644735829543',
    'if-modified-since': 'Sun, 13 Feb 2022 06:50:00 GMT',
    'referer': 'https://pvp.qq.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
}
start_source = requests.get(start_url, headers=headers).json()
print(start_source)
for hero in start_source:
    print(hero)
    hero_link = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(hero['ename'])
    # 为每个英雄单独创建文件夹保存皮肤
    try:
        os.mkdir('./王者荣耀皮肤采集/{}'.format(hero['cname']))
    except:
        print('文件夹已存在！！')
    # 请求获取每个英雄详情页面源码
    hero_source = requests.get(hero_link, headers=headers).content.decode('gbk')
    # print(hero_source)
    # 解析英雄所有皮肤数量
    regex = '<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">'
    pattern = re.compile(regex, re.S)
    hero_name = pattern.findall(hero_source)[0].split('|')
    # 解析英雄默认背景图片链接
    hero_pic_link = 'https:' + '//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-1.' \
                               'jpg'.format(hero['ename'], hero['ename'])
    print(hero_name, hero_pic_link)
    for i in range(len(hero_name)):
        pic_name = hero_name[i].split('&')[0]
        pic_link = 'https:' + '//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.' \
                              'jpg'.format(hero['ename'], hero['ename'], i + 1)
        print(pic_name, pic_link)
        pic_source = requests.get(pic_link, headers=headers).content
        with open('./王者荣耀皮肤采集/{}/{}_{}.jpg'.format(hero['cname'], i + 1, pic_name), 'wb') as file:
            file.write(pic_source)
    print('{}英雄皮肤下载完成！！'.format(hero['cname']))
    time.sleep(2)
