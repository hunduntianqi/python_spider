"""
    验证码:
        是门户网采用的一种反爬机制
    识别验证码:
        1. 人工肉眼识别(不推荐使用)
        2. 第三方自动识别(推荐使用)
            超级鹰使用流程:
                1. 导入超级鹰打码平台提供的Python Chaojiying_Client类
                2. 创建Chaojiying_Client类对象
                3. 调用对象方法PostPic(im, 1902)识别验证码
                    im: 验证码图片文件对象
                    1902: 识别的验证码类型
"""

# 示例:识别古诗文网验证码
# 1. 将验证码图片进行下载
# 2. 识别验证码

# 导入超级鹰打码平台提供的方法类
from chaojiying import Chaojiying_Client
import requests
from lxml import etree

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)
tree = etree.HTML(response.text)
img_url = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(img_url, headers=headers)
with open('./chaojiyingTest.jpg', 'wb') as file:
    file.write(img_data.content)
# 创建超级鹰对象
codeTest = Chaojiying_Client('17320101759', '2251789949gpt', '919742')
# 识别验证码
im = open('./chaojiyingTest.jpg', 'rb')
code = codeTest.PostPic(im, 1902)
print(code)