"""
    requests模块进阶学习:
        查询参数 ==> params:
            数据类型为字典, 可以对url地址中的查询参数进行编码拼接
            res = requests.get(url=baseurl, params=params, headers=headers)
            注意:url为基准url, 不包含查询参数, 且params会自动进行编码后与url拼接
        verify参数:
            参数值: True(默认)或False
            适用网站: https类型网站但是没有经过证书认证机构认证的网站
            适用场景: 当程序中抛出SSLError异常则考虑使用此参数
        代理ip参数 ==> proxies:
            作用: 代替自己原来的IP地址去对接网络的IP地址, 隐藏自身真实IP, 避免被网站封掉
            代理ip定义语法:
                proxies = {'协议':'协议://IP:端口号'}
                例:
                    proxies = {
                        'https': 'https://183.173.140.145:10080',
                        'http': 'http://183.173.140.145:10080'
                    }
            使用方式:
                res = requests.get / post(url, proxies=proxies)
            代理ip分类:
                高匿代理: web站点只能看到代理IP
                普通代理: Web站点知道请求是通过代理IP访问的, 但是不知道用户真实IP
                透明代理: Web站点既能看到代理IP, 又能看到用户真实IP
            私密代理和独享代理:
                使用需要用户名和密码的认证, 用户名和密码在对应代理IP网站上查找
                使用语法格式:
                    proxies = {
                        '协议':'协议://用户名:密码@IP:端口号'
                    }
"""
