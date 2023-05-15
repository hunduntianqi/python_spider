"""
    窗口切换:
        使用selenium操作浏览器多窗口切换
        相关方法:
            web_object.switch_to.window(窗口句柄):切换到相应窗口
                窗口句柄 ==> 类似于序列索引, 从 0 开始, 最后一个窗口为 -1
            web_object.current_window_handle: 获得当前窗口句柄
            web_object.window_handles: 获得所有窗口的句柄
    多表单切换:
        switch_to.frame()方法:
            将当前定位的主体切换到frame/iframe表单的内嵌页面中
            使用方法:
                1. 先定位到iframe:
                    xpath定位:xf = web_object.find_element('xpath', 'xpath_value')
                2. 将定位对象传给switch_to.frame()方法
                    web_object.switch_to.frame(xf)
                3. 操作完毕跳出当前一级表单:
                    switch_to.parent_content(): 该方法默认对应于离它最近的switch_to.frame()方法
                    跳出多级表单:
                        switch_to.default_content():跳回最外层页面
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys  # 导入此模块,可以模拟键盘输入
import time

if __name__ == '__main__':
    # 创建浏览器对象
    web = Chrome()
    web.get('http://lagou.com')
    # 找到某个元素-find_element('By_type', 'str')
    el = web.find_element('xpath', '//*[@id="changeCityBox"]/p[1]/a')
    # 点击找到的元素
    el.click()
    time.sleep(1)
    # 找到输入框,输入要搜索的内容
    web.find_element('xpath', '//*[@id="search_input"]').send_keys('python', Keys.ENTER)
    # time.sleep(1)
    # 点击职位名称,打开职位详情信息页面
    web.find_element('xpath', '//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').click()
    # selenium视角在原来的窗口中,需要切换到新窗口
    web.switch_to.window(web.window_handles[-1])  # 切换到最后一个窗口
    # 获取招聘信息
    job_data = web.find_element('xpath', '//*[@id="job_detail"]').text
    print(job_data)
    # 关掉当前窗口
    web.close()
    # 切换到第一个窗口
    time.sleep(1)
    web.switch_to.window(web.window_handles[0])
    web.close()
