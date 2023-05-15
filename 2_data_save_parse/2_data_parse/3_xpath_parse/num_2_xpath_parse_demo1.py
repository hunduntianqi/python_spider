"""
    xpath解析实战一 ==> 爬取58二手房房源信息
"""
# 导入相关模块
import time
import requests
from lxml import etree
import pymysql

if __name__ == '__main__':
    # 创建链接对象链接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='2251789949gpt', database='pythonstudy')
    # 创建游标对象
    cursor = conn.cursor()
    # 定义请求头
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
    }
    start_url = 'https://bj.58.com/ershoufang/p{}'
    for i in range(5, 6):
        # 定义请求url
        url = start_url.format(i + 1)
        # 发送请求获取响应数据
        page_text = requests.get(url=url, headers=headers)
        # 构建etree对象
        tree = etree.HTML(page_text.text)
        fangyuan_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
        print(len(fangyuan_list))
        # 便历获取对应标签对象
        for fangyuan in fangyuan_list:
            title: str = fangyuan.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0].strip()
            price: str = fangyuan.xpath('./a/div[2]/div[2]/p[2]/text()')[0].strip()
            all_price: str = fangyuan.xpath('./a/div[2]/div[2]/p[1]/span[1]/text()')[0].strip() + '万'
            print(title, price, all_price)
            # 定义sql语句
            sql = 'insert into ershoufang values(%s, %s, %s)'
            # 使用游标将数据写入数据库
            cursor.execute(sql, [title, price, all_price])
            # 数据提交数据库
            conn.commit()
        time.sleep(1)
        print('第{}页数据抓取完毕！！'.format(i + 1))
    # 关闭游标
    cursor.close()

    # 与数据库断开链接
    conn.close()
