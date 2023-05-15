from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time

options = ChromeOptions()
options.binary_location = r'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# 创建浏览器对象
web = Chrome(options=options)

web.get('https://www.lagou.com/')
time.sleep(3)

web.find_element('xpath', '//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element('xpath', '//*[@id="search_input"]').send_keys('Python', Keys.ENTER)
a_list = web.find_elements('class name', 'item__10RTO')
for a in a_list:
    time.sleep(1)
    # 以下两行代码解决元素页面超出视野无法点击的异常
    el = a.find_element('tag name', 'a')
    web.execute_script("arguments[0].click();", el)
    # 切换窗口视野为新打开的窗口
    web.switch_to.window(web.window_handles[-1])
    time.sleep(2)
    # 关闭新打开的子窗口
    web.close()
    time.sleep(2)
    web.switch_to.window(web.window_handles[-1])
    time.sleep(2)
    # 拿出与职位相关的文本数据
    text = web.find_element('xpath', '//*[@id="container"]/div[1]').text
    print(text)
    web.close()
    # 切换视野为原来的窗口
    web.switch_to.window(web.window_handles[0])
    # break
time.sleep(3)
# web.close()
