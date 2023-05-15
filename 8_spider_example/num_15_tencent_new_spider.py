"""
    腾讯新闻数据抓取
"""
import time
from pyquery import PyQuery
import requests


# 腾讯新闻今日要闻数据抓取
def today_important():
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://news.qq.com',
        'referer': 'https://news.qq.com/',
        'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    date = time.strftime('%Y_%m_%d')
    print('今日时间:{}'.format(date))
    url = 'https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=news_top_2018'
    response = requests.get(url, headers=headers)
    print(response.json())
    for text in response.json()['data']:
        title = text['title']
        text_url = text['url']
        print(title, text_url)
        response_text = requests.get(text_url, headers=headers)
        response_text.encoding = 'gbk'
        pq_pqrse = PyQuery(response_text.text)
        data = pq_pqrse('.content-article').text()
        print(data)
        time.sleep(1)


# 腾讯新闻今日话题数据抓取
def today_topic():
    date = time.strftime('%Y_%m_%d')
    print('今日时间:{}'.format(date))
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://news.qq.com',
        'referer': 'https://news.qq.com/',
        'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    url = 'https://i.news.qq.com/trpc.qqnews_web.pc_base_srv.base_http_proxy/NinjaPageContentSync?pull_urls=today_topic_2018'
    response = requests.get(url, headers=headers)
    print(response.json())
    for text in response.json()['data']:
        title = text['title']
        text_url = text['url']
        print(title, text_url)
        text_response = requests.get(text_url, headers=headers)
        text_response.encoding = 'gbk'
        pq_parse = PyQuery(text_response.text)
        data = pq_parse('.content-article').text()
        print(data)
        time.sleep(1)


# 腾讯新闻热点精选数据抓取
def hot_spot_select():
    date = time.strftime('%Y_%m_%d')
    print('今日时间:{}'.format(date))

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://news.qq.com',
        'referer': 'https://news.qq.com/',
        'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    for i in range(10):
        # data = {
        #     'sub_srv_id': '24hours',
        #     'srv_id': 'pc',
        #     'offset': '{}'.format(i * 20),
        #     'limit': '20',
        #     'strategy': '1',
        #     'ext': '{%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
        # }
        url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=' + str(
            i * 20) + '&limit=20&strategy=1&ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}'
        # 请求获取json数据
        response = requests.get(url, headers=headers)
        print(response.json())
        if len(response.json()['data']['list']) > 0:
            for text in response.json()['data']['list']:
                title = text['title']
                text_url = text['url']
                print(title, text_url)
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    hot_spot_select()