"""
    requests.post()请求方法:
        使用场景:Post类型请求的网站
        res = requests.post(url=url, data=data, headers=headers)
        data: 类型为字典, 包含post请求需要的表单参数
        post请求特点 ==> 以From表单方式提交数据
    扩展 ==> hashlib模块 ==> md5加密:
        md5加密:hashlib.md5
        h1 = hasnlib.md5()
        加密代码:
            h1.update(str.encode(encoding='utf-8'))
            hl.hexdigest() # 获取加密后数据
"""

import requests
import time
import random
import hashlib

if __name__ == '__main__':
    kw = input('请输入你要翻译的单词:')
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    h1 = hashlib.md5()  # 创建MD5加密算法对象
    lts = str(int(time.time() * 1000))
    print(lts)
    str_bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    h1.update(str_bv.encode())  # 加密str_bv字符串
    bv = h1.hexdigest()
    print(bv)
    salt = lts + str(random.randint(0, 9))
    print(salt)
    str_sign = "fanyideskweb" + kw + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
    h1.update(str_sign.encode())
    sign = h1.hexdigest()
    print(sign)
    data = {
        'i': kw,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': '"FY_BY_DEFAULT',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '270',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'OUTFOX_SEARCH_USER_ID=-126795918@10.169.0.82; JSESSIONID=aaaCvs4EmYWDJ79pQtr6x; OUTFOX_SEARCH_USER_ID_NCOO=614761249.3526307; ___rl__test__cookies=1643115573718',
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    res = requests.post(url=url, data=data, headers=headers)
    print(res.text)
