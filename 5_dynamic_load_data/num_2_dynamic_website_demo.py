"""
    动态加载网站数据抓取实战 ==> 小米应用商店信息抓取
"""
import random
import time
import requests, json

# url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://app.mi.com/category/2',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

app_list = []
for id in range(10):
    for i in range(3):
        url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'.format(i, id)
        res = requests.get(url=url, headers=headers)
        # res = json.loads(res.text)
        # print(res.status_code)
        # print(res.url)
        # print(res.json())
        for app in res.json()['data']:
            # print(app)
            app_dict = {}
            app_dict['name'] = app['displayName']
            app_dict['level1CategoryName'] = app['level1CategoryName']
            app_dict['packageName'] = 'https://app.mi.com/details?id=' + app['packageName']
            app_list.append(app_dict)
            print(app_dict)
        print('====================')
        time.sleep(random.randint(1, 2))
print(app_list)
with open('./app.js', 'w', encoding='utf-8') as file:
    json.dump(app_list, file, ensure_ascii=False)
