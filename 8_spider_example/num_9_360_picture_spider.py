"""
    selenium + Chrome 360 图片爬取
"""
import os
import requests
import time

# 导入浏览器驱动模块
from selenium.webdriver import Chrome
# 导入谷歌浏览器配置模块
from selenium.webdriver import ChromeOptions
# 导入键盘事件模块
from selenium.webdriver.common.keys import Keys


def pic_down(i, num, web, keyword):
    '''下载图片'''
    pic_data = web.find_element('xpath', 
        '//*[@id="searchlist"]/div[1]/ul[{}]/li[{}]/div/a/span[1]/img'.format(i, num))
    pic_link = pic_data.get_attribute('src')
    pic_nmae = pic_link.split('/')[-1].split('?')[0]
    print(pic_link, pic_nmae)
    flag = 0
    try:
        res_pic = requests.get(pic_link, timeout=2)
        with open('./{}/{}_{}_{}_{}'.format(keyword, type, i, num, pic_nmae), 'wb') as file:
            file.write(res_pic.content)
        if flag == 3:
            return
    except:
        pic_down(i, num, web, keyword)
        flag += 1


# 定义代理IP列表
# file = open('../2022_1_24_requests高级/ip_Pool.csv', 'r', encoding='utf-8')
# list_proxies = file.readlines()
# file.close()
start = time.time()
# 定义变量储存配置浏览器启动属性
options = ChromeOptions()
# 设置隐身模式
# options.add_argument('--incognito')
# 避免被检测
options.add_argument('--disable-infobars')
# 窗口最大化
options.add_argument('--start-maximized')
# 创建谷歌浏览器驱动对象
web = Chrome(options=options)
# 定义url
start_url = 'https://image.so.com/i'
# 打开浏览器
web.get(start_url)
# 输入查询关键字
keyword = input('请输入要查询的图片关键字:')
# 创建文件夹保存图片
try:
    os.mkdir('./{}'.format(keyword))
except:
    print("文件夹已存在！！")
# 根据关键字查询图片
web.find_element('xpath', '//*[@id="search_kw"]').send_keys(keyword, Keys.ENTER)
try:
    web.find_element('xpath', '//*[@id="chacha_tab_propmt"]/span[2]').click()
except:
    pass
count = int(input('请输入您想要加载的图片页数:'))
# 点击获取古装类型图片页
web.find_element('xpath', '//*[@id="tag"]/div/ul/li[2]/a').click()
# 定义变量存储图片遍历次数
num1 = 0
num2 = 0
num3 = 0
num4 = 0
flag = 1
load_num = 1
while flag:
    for i in range(1, 5):
        time.sleep(1)
        li_list = web.find_elements('xpath', '//*[@id="searchlist"]/div[1]/ul[{}]/li'.format(i))
        print('ul{}:{}'.format(i, len(li_list)))
        if i == 1 and len(li_list) != 0:
            if num1 >= len(li_list):
                flag = 0
                break
            for li_num in range(num1, len(li_list)):
                num1 += 1
                pic_down(i, num1, web, keyword)
        elif i == 2 and len(li_list) != 0:
            if num2 >= len(li_list):
                flag = 0
                break
            for li_num in range(num2, len(li_list)):
                num2 += 1
                pic_down(i, num1, web, keyword)
        elif i == 3 and len(li_list) != 0:
            if num3 >= len(li_list):
                flag = 0
                break
            for li_num in range(num3, len(li_list)):
                num3 += 1
                pic_down(i, num3, web, keyword)
        elif i == 4 and len(li_list) != 0:
            if num4 >= len(li_list):
                flag = 0
                break
            for li_num in range(num4, len(li_list)):
                num4 += 1
                pic_down(i, num4, web, keyword)
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 拖动滚动条到底部
    if load_num >= count:
        flag = 0
    load_num += 1
    time.sleep(1)
    print('----------------')
web.close()
end = time.time()
print('time: {}'.format(end - start))
