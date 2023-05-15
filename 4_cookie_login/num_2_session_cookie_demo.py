"""
    session模块实战 ==> 登录训练
"""
import requests, json

if __name__ == '__main__':
    # 创建session会话对象
    session = requests.session()
    # 构造请求头，避免被反爬虫
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    try:
        # 如果能读取到cookies文件, 执行以下代码, 跳过except的代码, 不用登录就能发表评论
        # 以reader读取模式, 打开名为cookies.txt的文件
        cookies_txt = open('./cookies.txt', 'r', encoding='utf-8')
        # 调用json模块的loads函数, 把字符串转成字典
        cookies_dict = json.loads(cookies_txt.read())
        # 把转成字典的cookies再转成cookies本来的格式
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        print(cookies)
        # 将已有 cookie 赋值给 session 对象中的 cookies
        session.cookies = cookies
    except FileNotFoundError:
        # 如果读取不到cookies文件, 程序报“FileNotFoundError”（找不到文件）的错, 则执行以下代码,
        # 重新登录获取cookies, 再评论
        # 登录的网址
        url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
        # 构造post请求表单参数
        data = {'log': 'hunduntianqi',  # input('请输入你的账号:'),
                'pwd': '2251789949gpt',  # input('请输入你的密码:'),
                'wp-submit': '登录',
                'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
                'testcookie': '1'}
        # 在会话下, 用post发起登录请求
        session.post(url, headers=headers, data=data)
        # cookie转换为字典
        cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
        # 调用json模块, 将字典转换为json格式字符串
        cookies_str = json.dumps(cookies_dict)
        # 创建文件存储cookie
        with open('./cookies.txt', 'w', encoding='utf-8') as file:
            file.write(cookies_str)

    # 请求url地址
    url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    # post请求表单参数构建
    data_1 = {
        'comment': input('请输入你想评论的内容：'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'

    }
    # 使用session发送post请求, 发表评论
    session.post(url_1, headers=headers, data=data_1)
