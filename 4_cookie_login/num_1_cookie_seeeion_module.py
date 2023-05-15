"""
    cookie:
        用来让服务器端记录客户端的相关状态, 因为http/https协议具有 无状态 的特性, 无法记录多个请求之间的关联性
        cookie是由多个 key=value 形式的参数组成, 使用 ';' 分割参数, 记录数据与用户状态
        处理cookie:
            1. 手动处理: 通过抓包工具获取cookie值, 将cookie封装到headers中
            2. 自动处理:
                cookie来源:模拟登录后, 由服务器端创建
                session会话对象:
                    创建session对象: session_object = requests.Session()
                    1. 可以进行请求的发送, 与requests模块一致
                    2. 在请求过程中产生的cookie, 会被自动存储在session对象中并携带
                    session对象发送get()或post请求:
                        res = session_object.post(url=url, data=data, headers=headers)
                        res = session_object.get(url=url, headers=headers)
                    获取cookies对象: cookies_object = session_object.cookies
                    cookie转换为字典: cookie_dict = requests.utils.dict_from_cookiejar(cookies_object)
                    字典转为cookie形式: cookie = requests.utils.cookiejar_from_dict(cookies_dict)
"""
