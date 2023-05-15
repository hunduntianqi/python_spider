import scrapy
from ..items import ScrapyexplainItem

'''
    爬虫文件
'''


class BaiduSpider(scrapy.Spider):
    # 爬虫名, 在启动项目时要用到: scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬虫爬取的域名, 只有在此域名下的网站才可以爬取
    allowed_domains = ['mapi.guazi.com']
    # 爬虫启动时起始url地址
    start_urls = []
    for i in range(1, 5):
        url = url = 'https://mapi.guazi.com/api/hometab/cartabH5?versionId=0.0.0.0&osv=android&sourceFrom=wap&pageNumber={}&deviceId=a4f16cd9-88c6-4272-f612-9d88b1ba6f26&guazi_city=103&platfromSource=wap'.format(
            i)
        start_urls.append(url)


    # 解析提取数据的函数, response: 下载器返回的响应对象,
    def parse(self, response):
        """解析提取数据 - 百度一下, 你就知道"""
        # scrapy响应对象集成了xpath, 可以直接使用xpath解析数据
        # response.xpath()执行结果: [<selector  xpath='' data='xxx'>], 为一个选择器对象列表
        #  例: [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # extract()方法: 提取列表中选择器对象中的字符串内容, 执行后结果:['字符串内容']
        # 例:['百度一下，你就知道']
        # extract_first()方法:提取列表中第一个选择器对象中的字符串内容
        # get()方法: 等同于extract_first()方法
        # item['title'] = response.xpath('/html/head/title/text()').get()
        item = ScrapyexplainItem()
        res = response.json()['data']['list']
        print(res)
        for i in range(len(res)):
            key_list = res[i].keys()
            try:
                if 'cellTag' in key_list:
                    data = res[i]['carList'][0]
                    item['name'] = data['title']
                    item['price'] = data['price']
                    item['link'] = 'https://www.guazi.com/Detail?clueId=' + data['clue_id']
                    yield item
                else:
                    item['name'] = res[i]['title']
                    item['price'] = res[i]['price']
                    item['link'] = 'https://www.guazi.com/Detail?clueId=' + res[i]['clue_id']
                    yield item
            except:
                pass
        # 一页数据爬取完毕, 生成下一页url
        # self.i += 1
        # if self.i == 5:
        #     return
        # url = 'https://mapi.guazi.com/api/hometab/cartabH5?versionId=0.0.0.0&osv=android&sourceFrom=wap&pageNumber={}&deviceId=a4f16cd9-88c6-4272-f612-9d88b1ba6f26&guazi_city=103&platfromSource=wap'.format(
        #     self.i)
        # # 把url交给调度器入队列
        # yield scrapy.Request(url=url, callback=self.parse)
        # callback = selc.parse: 指定解析函数, parse是函数名
