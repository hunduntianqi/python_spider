import scrapy
from ..items import KfcadressItem


class KfcadressSpider(scrapy.Spider):
    name = 'kfcadress'
    allowed_domains = ['www.kfc.com.cn']
    # 重写start_request方法
    city_name = input('请输入你要查询的地区关键字:')
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    # 重写start_requests方法, 获取城市门店总数量
    def start_requests(self):
        formdata = {
                'cname': self.city_name,
                'pid': '',
                'keyword': '',
                'pageIndex': str(1),
                'pageSize': '10'
            }
        # 交给调度器入队列
        yield scrapy.FormRequest(url=self.post_url, formdata=formdata, callback=self.get_tatol_page)

    def get_tatol_page(self, response):
        res = response.json()['Table'][0]
        count = res['rowcount']
        print(count)
        tatol_page = count / 10 if count % 10 == 0 else count / 10 + 1
        for i in range(int(tatol_page)):
            formdata = {
                'cname': self.city_name,
                'pid': '',
                'keyword': '',
                'pageIndex': str(i + 1),
                'pageSize': '10'
            }
            # 将请求交给调度器入队列
            yield scrapy.FormRequest(url=self.post_url, formdata=formdata, callback=self.parse, dont_filter=True)


    def parse(self, response):
        item = KfcadressItem()
        res = response.json()['Table1']
        print(res)
        for data in res:
            item['rownum'] = data['rownum']
            item['storeName'] = data['storeName']
            item['addressDetail'] = data['addressDetail']
            item['pro'] = data['pro']
            item['cityName'] = data['cityName']
            item['provinceName'] = data['provinceName']
            print(data)
            yield item


