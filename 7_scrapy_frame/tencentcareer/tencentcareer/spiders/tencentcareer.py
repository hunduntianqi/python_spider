import scrapy
from urllib import parse
from ..items import TencentcareerItem


class TencentcareerSpider(scrapy.Spider):
    name = 'tencentCareer'
    allowed_domains = ['careers.tencent.com']
    word = input('请输入您要搜索职位的关键字:')
    result = parse.quote(word)

    def start_requests(self):
        start_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex=1&pageSize=10'.format(
            self.result)
        yield scrapy.Request(url=start_url, callback=self.get_page_total)

    def get_page_total(self, response):
        res = response.json()['Data']
        count = res['Count']
        if count % 10 == 0:
            page_total = count / 10
        else:
            page_total = int(count / 10) + 1
        print('总页数为:{}'.format(page_total))
        for page in range(int(page_total)):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex={}&pageSize=10'.format(
                self.result, page + 1)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        res = response.json()['Data']["Posts"]
        print(res)
        for link in res:
            job_data_link = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId=' + link['PostId']
            print(job_data_link)
            yield scrapy.Request(url=job_data_link, callback=self.data_parse)

    def data_parse(self, response):
        item = TencentcareerItem()
        res = response.json()['Data']
        item['job_name'] = res['RecruitPostName'].strip()
        item['job_address'] = res['LocationName'].strip()
        item['job_type'] = res['CategoryName'].strip()
        item['job_time'] = res['LastUpdateTime'].strip()
        item['job_responsibility'] = res['Responsibility'].strip()
        item['job_requirement'] = res['Requirement'].strip()
        print(item)
        yield item
