"""
    urllib.parse编码模块:
        作用:对url地址中的中文进行编码, 解决中文乱码问题, 通常用于给查询参数编码
        导入模块
            1. import urllib.parse
            2. from urllib import parse
        示例:
            编码前:https://www.baidu.com/s?wd=美女
            编码后:https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
        urlencode()方法:
            作用:给url地址中查询参数进行编码, 参数类型为字典
            示例:
                编码前:params = {'wd':'美女'}
                编码中:params = urllib.parse.urlencode(params)
                编码后:params结果:'wd=%E7%BE%8E%E5%A5%B3'
            多个查询参数:params = {'参数1':'值1', '参数2':'值2', ...}
            urlencode()方法会自动对多个查询参数之间添加&符号链接
        quote()方法:
            作用: 给url地址中的查询参数进行编码, 参数类型为字符串
            示例:
                word = '美女'
                result = urllib.parse.quote(word)
                result结果:'wd=%E7%BE%8E%E5%A5%B3'
        unquote()方法:
            作用:将编码后的字符串转为普通的Unicode字符串
            示例:
                params = 'wd=%E7%BE%8E%E5%A5%B3'
                result = parse.unquote(params)
                result结果:美女
"""
# 导入request模块和parse模块
from urllib import request, parse
from fake_useragent import UserAgent


def urlencode_test():
    # 1. 拼接url地址
    word = input('请输入搜索关键字:')
    params = parse.urlencode({'wd': word})
    url = 'http://www.baidu.com/s?{}'.format(params)
    print(url)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Host": "www.baidu.com"
    }
    # 2. 构建请求对象
    req = request.Request(url=url, headers=headers)
    # 3. 发送请求获取响应对象
    res = request.urlopen(req)
    # 获取响应状态码
    print(res.getcode())
    # 获取返回响应数据的具体URL
    print(res.geturl())
    # 获取响应内容
    html = res.read().decode()
    print(html)


def quote_test():
    # 1. 拼接URL地址
    url = "http://www.baidu.com/s?wd={}".format(parse.quote(input('请输入搜索关键字:')))
    # 构造请求头
    ua = UserAgent().Chrome
    print(ua)
    headers = {
        'user-agent': ua
    }
    # 构建请求对象
    req_object = request.Request(url, headers=headers)
    # 发送请求获取响应对象
    response_object = request.urlopen(req_object)
    print(type(response_object))
    # 获取响应内容
    res_data = response_object.read().decode()
    print(res_data)
    print(response_object.getcode())
    print(response_object.geturl())


if __name__ == '__main__':
    # urlencode_test()
    quote_test()