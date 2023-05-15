"""
    使用spider实现有道查单词效果
"""
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    while True:
        try:
            url = 'http://www.youdao.com/w/eng/{}/#keyfrom=dict2.index'.format(input('请输入要查询的单词:'))
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
            res = requests.get(url, headers=header)
            data = BeautifulSoup(res.text, 'lxml')
            yiwen_list = data.find('div', class_="trans-container").find_all('li')
            for i in yiwen_list:
                yiwen = i.text.strip()
                print(yiwen)
            kw = input('是否继续查询单词(Y/N):')
            if kw == 'N' or kw == 'n':
                break
            else:
                pass
        except:
            print('错误！！！请输入英文单词')
