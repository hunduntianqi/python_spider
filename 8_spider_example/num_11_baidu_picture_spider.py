"""
    百度图片抓取
"""
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# 封装函数, 方便调用
def work(web, header, proxies, save):
    # for i in range(70):
    #     web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(0.5)

    for num in range(1, 20):
        web.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 拖动滚动条到底部
        time.sleep(0.5)
        for j in range(22):
            flag = web.find_elements_by_xpath('//*[@id="imgid"]/div[{}]/ul/li[{}]/a'.format(num, j))
            # //*[@id="imgid"]/div[3]/ul/li[22]/div[1]/div[2]/a/img
            # //*[@id="imgid"]/div[4]/ul/li[22]/a
            # //*[@id="imgid"]/div[9]/ul/li[4]/div/div[2]/a/img
            # //*[@id="imgid"]/div[9]/ul/li[5]/div[1]/div[2]/a/img
            # //*[@id="imgid"]/div[9]/ul/li[6]/div/div[2]/a/img
            print(flag)
            if len(flag) != 0:
                name = web.find_element_by_xpath('//*[@id="imgid"]/div[{}]/ul/li[{}]/a'.format(num, j)).get_attribute(
                    'title').strip().replace("|", "_")
                print(name)
                try:
                    picUrl = web.find_element_by_xpath(
                        '//*[@id="imgid"]/div[{}]/ul/li[{}]/div/div[2]/a/img'.format(num, j)).get_attribute('src')
                    print(picUrl)
                    picres = requests.get(picUrl, headers=header, proxies=proxies)
                    picres.encoding = "utf-8"
                except:
                    print("图片链接异常！！")
                try:
                    with open(r'./{}/{}_.{}_.jpg'.format(save, (num - 1) * 22 + j, name), "wb") as f:
                        f.write(picres.content)
                    print("pic{}_:{}下载成功！！".format((num - 1) * 22 + j, name))
                    time.sleep(0.5)
                except:
                    print("pic{}_:{}下载失败！！".format((num - 1) * 22 + j, name))
            else:
                print('no pic!!')


def picDown(web):
    # 清空输入框并输入要搜索的图片关键字
    web.find_element_by_xpath('//*[@id="kw"]').clear()
    web.find_element_by_xpath('//*[@id="kw"]').send_keys(input("请输入您要下载的美图关键词\n"), Keys.ENTER)

    save = input("请输入要存储文件的文件夹名称:\n")
    # 创建文件夹存储图片
    try:
        os.mkdir(r'./{}'.format(save))
    except:
        print("目标文件夹已存在！！")

    proxies = {
        """
        'http':'http://代理IP地址',要请求的网站开头为http
        'https':'https://代理IP地址'要请求的网站开头为https
        """
        'https': '27.191.60.175:3256'
    }

    # 构建请求头
    header = {
        'Referer': 'https://image.baidu.com/',  # 防盗链
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    t1 = time.time()
    # 创建多线程
    with ThreadPoolExecutor(1000) as speedUp:
        speedUp.submit(work, web=web, header=header, proxies=proxies, save=save)
    time.sleep(5)
    # web.close()
    t2 = time.time()
    print("共用时:{}秒".format(t2 - t1))


if __name__ == '__main__':
    opt = Options()
    # opt.add_argument('--headless')
    opt.add_argument('--disable-blink-features=AutomationControlled')
    web = Chrome(options=opt)  # 创建浏览器对象
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1640353761702_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDIsMSw2LDQsNSw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E5%8F%A4%E8%A3%85%E7%BE%8E%E4%BA%BA%E5%9B%BE"
    # 打开浏览器
    web.get(url)
    web.maximize_window()
    # 定义10s延迟, 避免因验证码造成异常
    time.sleep(10)
    picDown(web)
    print("end!!")
    web.close()
