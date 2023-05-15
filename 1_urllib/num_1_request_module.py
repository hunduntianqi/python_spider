"""
    urllib.request模块-python标准库:
        作用:向网站发出请求
        request.urlopen()-获取一个响应对象:
            作用:向网站发出请求并获取响应对象
            参数:
                url: 需要爬取的网站地址
                timeout: 设置等待超时时间, 指定时间内未响应抛出超时异常
            响应对象方法:
                1. read(): 返回数据类型为bytes, 需要使用decode()方法转换为字符串
                2. geturl(): 返回实际数据的url地址
                3. getcode(): 返回http响应码
    请求头 ==> headers:
        是网站用来判断请求来源的参数, 以此判断是不是正常的浏览器请求
        测试网站: http://httpbin.org/get
        向测试网站发请求, 会返回请求头内容
        User-Agent: 请求头中用来判断浏览器类型的参数, 服务器以此判断是哪中浏览器发送的请求
        urllib.request.Request():
            作用: 包装请求头, 包装完成后使用urlopen()方法发送请求
            参数:
                url: 需要爬取的网站地址
                headers: 包装后的请求头数据, 类型为字典, 例: headers = {'User-Agent':'伪装的浏览器请求头'}
        携带请求头发送请求:
            1. 构造请求对象: req = request.Request(url=url, headers=headers)
            2. 获取响应对象: res = request.urlopen(req)
            3. 获取响应内容: html = res.read().decode()
        from fake_useragent import UserAgent模块:
            可以用来随机生成任意类型浏览器的UA(User-Agent)
            UserAgent().random ==> 可以获取任意浏览器的请求头
            UserAgent().Chrome ==> 可以获取谷歌浏览器的请求头
            UserAgent().firefox ==> 可以获取火狐浏览器的请求头
"""
# 导入模块
from urllib import request


def request_test():
    res = request.urlopen(url="http://www.baidu.com/", timeout=3000)
    # 响应对象方法read(), 解析获取响应数据为文本形式
    html = res.read().decode('utf-8')
    print(html)
    # 获取返回响应数据的URL
    print(res.geturl())
    # 获取响应状态码
    print(res.getcode())


def headers_test():
    # 定义URL
    url = 'http://httpbin.org/get'
    # 定义请求头数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    # 包装请求头
    req = request.Request(url=url, headers=headers)
    # 获取响应对象
    res = request.urlopen(req)
    # 获取响应内容
    html = res.read().decode()
    # 打印输出
    print(html)


if __name__ == '__main__':
    request_test()
    # headers_test()
