import os
import sys
import threading
import time

import requests
from bs4 import BeautifulSoup


# 定义函数, 提取大图链接地址
def get_big_url(pic_url: str, headers: dict):
    # 发送请求, 获取大图页面数据
    resp = requests.get(pic_url, headers=headers)
    resp.encoding = "gbk"
    # 创建soup对象
    soup_big = BeautifulSoup(resp.text, 'lxml')
    # 解析数据获取大图链接
    big_url = 'https://pic.netbian.com' + soup_big.find('a', id='img').find('img')['src']
    print(big_url)
    return big_url


# 定义函数, 下载图片
def down_pic(url: str, pic_name: str, headers: dict):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'gbk'
    pic_data = resp.content
    with open('./4k/{}.jpg'.format(pic_name), 'wb') as file:
        file.write(pic_data)
        file.flush()


if __name__ == '__main__':
    start = time.time()
    # 创建文件夹, 保存图片数据
    try:
        os.mkdir('./4K')
    except:
        pass
    # 定义url
    url = ""  # type:str
    # 定义请求头
    headers: dict = {
        'cookie': '__yjs_duid=1_dd88f8e6b75e546b9003fca6eea84f861683550325513; zkhanecookieclassrecord=%2C54%2C; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1683550317,1683629683,1683719873,1683804851; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1683808248; yjs_js_security_passport=e794bbb781e4ab7799d4a0a7869867a9e998f021_1683811834_js',
        'referer': 'https://pic.netbian.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # 定义变量, 计数
    num: int = 1
    while True:
        if num == 1:
            url = "https://pic.netbian.com/4kmeinv/"
        else:
            url = "https://pic.netbian.com/4kmeinv/index_{}.html".format(num)
        # 发送请求
        response = requests.get(url, headers=headers)
        # 修改文本编码
        response.encoding = "gbk"
        print(response.text)
        # 创建BeautifulSoup对象
        soup = BeautifulSoup(response.text, 'lxml')
        # 解析获取图片所在标签 li 列表
        li_list = soup.find('div', class_='slist').find_all('li')
        for li in li_list:
            # print(li)
            pic_name = li.find('b').text
            pic_url = 'https://pic.netbian.com' + li.find('a')['href']
            print("{} ==> {}".format(pic_name, pic_url))
            big_url = get_big_url(pic_url, headers)
            thread = threading.Thread(target=down_pic, args=(big_url, pic_name, headers))
            thread.start()
            # 调用函数, 下载图片
            # down_pic(big_url, pic_name, headers)
        print("第{}页数据抓取完毕!!".format(num))
        if "下一页" in response.text:
            num += 1
        else:
            end = time.time()
            print("数据抓取完毕, 共耗时 ==> {} s".format(end - start))
            time.sleep(3)
            # 退出系统
            sys.exit()
