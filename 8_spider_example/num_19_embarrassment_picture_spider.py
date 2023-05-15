"""
    糗事百科图片抓取
"""
import re
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}
obj = re.compile(r'<span>(?P<name>.*?)</span>.*?<div class="thumb">.*?<img src="(?P<pic_link>.*?)" alt.*?'
                 r'</a>.*?</div>', re.S)
num = 1
while True:
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(num)
    res = requests.get(url, headers=header)
    data = obj.finditer(res.text)
    # print(data)
    if data == []:
        break
    else:
        num += 1
    for pic in data:
        pic_name = pic.group('name').strip()
        print(pic_name)
        pic_link = 'https:' + pic.group('pic_link').strip()
        print(pic_link)
        pic_res = requests.get(pic_link, headers=header)
        pic_data = res.content
        with open('./糗事百科糗图/{}.jpg'.format(pic_name), 'wb') as file:
            file.write(pic_data)
