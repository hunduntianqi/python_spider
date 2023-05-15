"""
    selenium实战 ==> qq邮箱登录操作
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    # 配置浏览器启动属性
    options = ChromeOptions()
    # 设置浏览器安装路径
    options.binary_location = r'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # 设置窗口最大化
    options.add_argument('--start-maximized')
    # 避免被检测
    options.add_argument('--disable-infobars')
    # 设置隐身模式
    options.add_argument('--incognito')
    # 禁用JavaScript
    # options.add_argument('--disable-javascript')
    # 无头浏览器
    # options.add_argument('--headless')
    # 创建Chrome浏览器对象
    web = Chrome(options=options)
    time.sleep(3)
    # 启动浏览器
    web.get('https://mail.qq.com/')
    # 定位登录页面内部表单
    login_frame = web.find_element('xpath', '//*[@id="login_frame"]')
    # 将定位主体切换到内部表单
    web.switch_to.frame(login_frame)
    web.find_element('xpath', '//*[@id="u"]').send_keys(input('请输入您的qq账号:'))
    web.find_element('xpath', '//*[@id="p"]').send_keys(input('请输入您的登录密码:'))
    web.find_element('xpath', '//*[@id="login_button"]').click()
    time.sleep(2)
    # 获取html页面结构源码
    print(web.page_source)
    # 获取登陆后页面标题
    print(web.title)
    # 获取登陆后页面url
    print(web.current_url)
    time.sleep(5)
    # 退出浏览器
    web.quit()
