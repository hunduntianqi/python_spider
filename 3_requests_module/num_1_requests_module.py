"""
    requests模块:
        作用: 类似于urllib, 向网站发送请求获取响应, 属于第三方模块, 使用前要先安装模块
        requests模块使用:
            response_object = requests.get(url, headers=headers, data=data) ==> Get请求
            response_object = response.post(url, headers=headers, data=data) ==> post请求
            获取文本内容:
                text = response_object.text
            获取状态响应码:
                statue_code = response_object.statu_code
            获取字节内容:
                content = response_object.content
            获取实际返回数据的url:
                url_data = response_object.url
            json数据转换为python形式:
                json_data = response_object.json()
"""
# 导入requests模块
import requests


if __name__ == '__main__':
    url = 'https://baidu.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
    }
    res = requests.get(url=url, headers=headers)
    print(res.status_code)
    print(res.text)