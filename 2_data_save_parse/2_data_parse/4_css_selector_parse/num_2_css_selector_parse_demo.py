"""
    使用pyquery模块进行css选择器解析实战 ==> 汽车之家信息抓取
"""
import time
import requests
import pyquery
import openpyxl


class QiCheKouBei():
    def __init__(self):
        self.url = 'https://k.autohome.com.cn/ajax/getSceneSelectCar?minprice=2&maxprice=110&_appid=koubei&level=3'
        self.headers = {
            'referer': 'https://k.autohome.com.cn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        self.data_list = ['车主id', '品牌', '购车地点', '购车时间', '裸车购买价', '油耗', '目前行驶里程', '空间评价',
                          '动力评价', '操控评价',
                          '油耗评价', '舒适性评价', '外观评价', '内饰评价', '性价比', '购车目的']
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(self.data_list)

    def start_data(self):
        response = requests.get(self.url, headers=self.headers)
        data = response.json()
        return data

    def url_parse(self, start_data):
        url_template = 'https://k.autohome.com.cn/{}/#pvareaid=2099124'
        url_list = []
        for car in start_data['result']:
            seriesId = car['seriesId']
            url = url_template.format(seriesId)
            url_list.append(url)
        return url_list

    def page_parse(self, start_url):
        seriesId = start_url.split('/')[-2]
        response = requests.get(start_url, self.headers)
        # 创建pyquery对象
        html = response.text
        p = pyquery.PyQuery(html)
        # css选择器解析评论页数
        page = p('.page-item-info').text()[1:][:-1]
        # 定义列表存储每页评论的url
        page_list = [start_url]
        if page == '':
            print('页数为空')
            return page_list
        else:
            print('页数为:{}'.format(page))
            for index in range(2, int(page) + 1):
                page_url = 'https://k.autohome.com.cn/{}/index_{}.html#dataList'.format(seriesId, index)
                page_list.append(page_url)
            return page_list

    def parse_data(self, page_url):
        response = requests.get(page_url, headers=self.headers)
        # print(response.text)
        # 创建Pyquery对象
        p = pyquery.PyQuery(response.text)
        it = p('.mouthcon-cont-left').items()
        for item in it:
            dl_num = len(item('.mt-10 > dl'))
            print(dl_num)
            if dl_num == 6:
                name = item('.name-text').text()
                car_type = item('.mt-10 > dl:nth-child(1) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_site = item('.mt-10 > dl:nth-child(2) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_time = item('.mt-10 > dl:nth-child(3) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_price = item('.mt-10 > dl:nth-child(4) > dd').text().replace(' ', '_').replace('\n', '_')
                fuel_con = item('.mt-10 > dl:nth-child(5) > dd > p:nth-child(1)').text().replace(' ', '_').replace('\n',
                                                                                                                   '_')
                now_length = item('.mt-10 > dl:nth-child(5) > dd > p:nth-child(2)').text().replace(' ', '_').replace(
                    '\n', '_')
                evaluate = item('.position-r > dl > dd > span:nth-child(2)').text().replace(' ', '_').replace(
                    '\n', '_')
                space = evaluate.split('_')[0] + '星'
                power = evaluate.split('_')[1] + '星'
                control = evaluate.split('_')[2] + '星'
                fuel = evaluate.split('_')[3] + '星'
                comfort = evaluate.split('_')[4] + '星'
                cosmetic = evaluate.split('_')[5] + '星'
                decorate = evaluate.split('_')[6] + '星'
                performance = evaluate.split('_')[7] + '星'
                buy_goal = item('.border-b-no > dd').text().replace(' ', '/').replace(
                    '\n', '/')
                print(name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                      control, fuel, comfort, cosmetic, decorate, performance, buy_goal)
                self.data_list.append(
                    [name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                     control, fuel, comfort, cosmetic, decorate, performance, buy_goal])
                self.sheet.append([name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                                   control, fuel, comfort, cosmetic, decorate, performance, buy_goal])
            else:
                name = item('.name-text').text()
                car_type = item('.mt-10 > dl:nth-child(1) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_site = item('.mt-10 > dl:nth-child(2) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_time = item('.mt-10 > dl:nth-child(4) > dd').text().replace(' ', '_').replace('\n', '_')
                buy_price = item('.mt-10 > dl:nth-child(5) > dd').text().replace(' ', '_').replace('\n', '_')
                fuel_con = item('.mt-10 > dl:nth-child(6) > dd > p:nth-child(1)').text().replace(' ', '_').replace('\n',
                                                                                                                   '_')
                now_length = item('.mt-10 > dl:nth-child(6) > dd > p:nth-child(2)').text().replace(' ', '_').replace(
                    '\n', '_')
                evaluate = item('.position-r > dl > dd > span:nth-child(2)').text().replace(' ', '_').replace(
                    '\n', '_')
                space = evaluate.split('_')[0] + '星'
                power = evaluate.split('_')[1] + '星'
                control = evaluate.split('_')[2] + '星'
                fuel = evaluate.split('_')[3] + '星'
                comfort = evaluate.split('_')[4] + '星'
                cosmetic = evaluate.split('_')[5] + '星'
                decorate = evaluate.split('_')[6] + '星'
                performance = evaluate.split('_')[7] + '星'
                buy_goal = item('.border-b-no > dd').text().replace(' ', '/').replace(
                    '\n', '/')
                print(name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                      control, fuel, comfort, cosmetic, decorate, performance, buy_goal)
                self.data_list.append(
                    [name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                     control, fuel, comfort, cosmetic, decorate, performance, buy_goal])
                self.sheet.append([name, car_type, buy_site, buy_time, buy_price, fuel_con, now_length, space, power,
                                   control, fuel, comfort, cosmetic, decorate, performance, buy_goal])
        time.sleep(1)

    def run(self):
        json_data = self.start_data()
        # print(json_data)
        url_list = self.url_parse(json_data)
        print(url_list)
        for url in url_list:
            page_list = self.page_parse(url)
            print(page_list)
            for page_url in page_list:
                self.parse_data(page_url)
            self.wb.save('./汽车之家口碑信息.xlsx')
            time.sleep(2)
        self.wb.close()


if __name__ == '__main__':
    spider = QiCheKouBei()
    spider.run()
