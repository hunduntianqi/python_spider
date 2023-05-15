"""
    快手短视频下载
"""
import os
import sys
import time
import requests
import json

keyword = input('请输入要搜索短视频的关键字:')
# 创建文件夹保存视频
try:
    os.mkdir('./kuaishou_movie_{}'.format(keyword))
except:
    print('文件夹已存在！！')
# 定义请求头
headers = {
    'accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '1088',
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_d5a4e943f10d3c05b37d753453fd4ff0; didv=1646528072421; client_key=65890b29; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjQ2OTIyMjQ3LjE2NDY1MzI4MDE4OTIuNDEzMDI3NA==|MS43NjQ1ODM2OTgyODY2OTgyLjIxNjk0OTI4LjE2NDY1MzI4MDE4OTIuNDEzMDI3NQ==|0|graphql-server|webservice|false|NA; userId=2244127339; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABGEAIF4tWX6Yjpc0FIbUuCNH50RErF8GSRrjy63oriajg908stf_fG9DjtrWhrUw22QRSl2I2Iwc2RgwZUtBAyHkRKj7hsYqcioZssiJicoE-hsbqFm5fps8hxSzjtvW03xb-jBuTDHdBnml7bBMmIsJnbsrmqMHNvPxPtrDqEHbTzNDI6giLm41iUuoAY6WZkNIet3_chDAMYtNptSHXIxoSoJCKbxHIWXjzVWap_gGna5KjIiCGQI_dwsLU1xJX-UCL0DHbYYvlL26_VyJdoiIe2gGkLSgFMAE; kuaishou.server.web_ph=10a19f9a7bf1d0b08f5568e2fcf558cc031e',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/brilliant',
    'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
# 定义url
url = 'https://www.kuaishou.com/graphql'
for i in range(10):
    if i == 0:
        fromdata = {
            'operationName': "visionSearchPhoto",
            'query': "query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n",
            'variables': {'keyword': "{}".format(keyword), 'pcursor': "", 'page': "search"}
        }
    else:
        fromdata = {
            'operationName': "visionSearchPhoto",
            'query': "query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n",
            'variables': {'keyword': "{}".format(keyword), 'page': "search", 'pcursor': "{}".format(i),
                          'searchSessionId': "MTRfMjI0NDEyNzMzOV8xNjQ2NTI5ODU0MzI2X-Wwj-aloF81MDEw"}
            # MTRfMjI0NDEyNzMzOV8xNjQ2NTMyOTEyMzUyX-Wwj-aloF_popzlgLxfODUzNQ
            # MTRfMjI0NDEyNzMzOV8xNjQ2NTI5ODU0MzI2X-Wwj-aloF81MDEw
        }
    fromdata = json.dumps(fromdata)  # 转换字典为json字符串
    # print(type(fromdata))
    response = requests.post(url, data=fromdata, headers=headers)
    print(response.json())
    # print(response.status_code)
    # print(response.json()['data']['brilliantTypeData']['feeds'])
    print(len(response.json()['data']['visionSearchPhoto']['feeds']))
    for movie in response.json()['data']['visionSearchPhoto']['feeds']:
        name = movie['photo']['caption'].strip().replace('#', '-井号').replace(',', '-逗号').replace('@',
                                                                                                     '-艾特号').replace(
            '!', '-感叹号').replace('?', '-问号').replace('➕', '-加号').replace('(', '-左括号').replace(')',
                                                                                                        '-右括号').replace(
            '。',
            '-句号').replace(
            '...', '-省略号').replace('.', '-点').replace('💗', '-emj').replace('❤', '-emj').replace('😂', '-emj') \
            .replace('，', '-中文逗号').replace('\n', '-换行符').replace('《', '左书名号').replace('》',
                                                                                                 '右书名号').replace(
            '"',
            '-引号').replace(
            '“',
            '-中文引号').replace('<', '-小于号').replace('>', '-大于号').replace('/', '-除号').replace('*',
                                                                                                       '-乘号').replace(
            '（',
            '-左括号') \
            .replace('）', '-右括号').replace('|', '-符号或').replace('&', '-符号与').replace('~', '-波浪线').replace(
            '$',
            '-美元符').replace(
            '^', '-幂符号').replace('%', '-百分号').strip()
        movie_link = movie['photo']['photoUrl']
        print(name, movie_link)
        headers_movie = {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cache-Control': 'max-age=0',
            # 'Connection': 'keep-alive',
            # 'Host': 'v1.kwaicdn.com',
            # 'If-Modified-Since': 'Fri, 04 Mar 2022 09:11:08 GMT',
            # 'Range': 'bytes=0-1048575',
            # 'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': '"Windows"',
            # 'Sec-Fetch-Dest': 'document',
            # 'Sec-Fetch-Mode': 'navigate',
            # 'Sec-Fetch-Site': 'none',
            # 'Sec-Fetch-User': '?1',
            # 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        movie_res = requests.get(movie_link, headers=headers_movie)
        with open('./kuaishou_movie_{}/{}.mp4'.format(keyword, name[:31]), 'wb') as file:
            file.write(movie_res.content)
        print('{}视频下载成功！！'.format(name))
