"""
    selenium:
        一种自动化测试工具, 可以打开浏览器, 然后像人一样操作浏览器, 程序员可以从selenium中直接提取网页上的各种信息
        环境搭建:
            1. 安装selenium模块 ==> pip install selenium
            2. 下载浏览器驱动(谷歌, 火狐, IE等)
            3. 把浏览器驱动文件放在python解释器所在的文件夹下
        selenium简单使用:
            1. 根据使用的浏览器导入对应模块:
                from selenium.webdriver import 对应浏览器(例: Chrome ==> 谷歌)
            2. 创建浏览器对象:
                web_object = 浏览器类() ==> 例: web = Chrome()
            3. 打开对应网站:
                web_object.get(url)
            4. 定位元素:
                a. 定位单个元素:
                    web_object.find_element('By_type', 'value')
                b. 定位多个元素:
                    web_object.find_elements('By_type', 'value')
                By_type:
                    定位元素选择器类型
                        ID = "id"
                        XPATH = "xpath"
                        LINK_TEXT = "link text"
                        PARTIAL_LINK_TEXT = "partial link text"
                        NAME = "name"
                        TAG_NAME = "tag name"
                        CLASS_NAME = "class name"
                        CSS_SELECTOR = "css selector"
        selenium常用操作:
            web_object.get(url): 地址栏输入url地址并确认
            web_object.quit(): 关闭浏览器
            web_object.close(): 关闭当前页
            web_object.maximize_window():浏览器窗口最大化
            web_object.page_source: HTML结构源码
            web_object.page_source.find('字符串'): 从源码中查找指定字符串, 没有返回-1, 常用于判断最后一页
            web_object.set__window_size(width, height): 设置浏览器窗口大小
            web_object.back(): 浏览器后退
            web_object.forward(): 浏览器前进
            web_object.refresh(): 模拟浏览器刷新当前页面
            web_object.title: 获得当且页面标题
            web_object.current_url: 获得当前页面的url
            web_object.get_screenshot_as_file(path): 窗口截图, 截取当前窗口并指定截图图片的保存位置
            元素对象.clear(): 清除文本内容
            元素对象.send_keys(*value): 模拟按键输入, value为输入内容
            元素对象.click(): 模拟浏览器单击元素
        WebElement接口常用方法:
            WebElement ==> 代表浏览器中的元素对象, 可以对元素进行操作
            1. submit(): 提交表单, 例如回车操作
            2. size: 返回元素的尺寸
                例:size = web_object.find_element_by_id('kw').size
            3. text: 返回元素的文本
                例:text = web_object.find_element_by_id('cp').text
            4. get_attribute(name): 获得元素的属性值, 可以是id, name, type或其他任意属性值
                例:attribute = web_object.find_element_by_id('kw').get_attribute('type')
            5. is_displayed(): 该元素是否用户可见, 返回结果为True或False
                例:result = web_object.find_element_by_id('kw').is_displayed()
        selenium操作js ==> 调用JavaScript:
            WebDriver提供了execute_script()方法来执行JavaScript代码
            例: 通过JavaScript设置滚动条位置
                window.scrollTop(左边距, 上边距)
                js = 'window.scrollTop(0, 450);'
                web_object.execute_script(js)
        selenium操作cookie:
            1. get_cookies(): 获得所有cookie信息
            2. get_cookie(name): 返回字典的键为“name”的cookie信息
            3. add_cookie(cookie_dict): 添加cookie, 'cookie_dict'指字典对象, 必须有name和value值
            4. delete_cookie(name, optionsString): 删除cookie信息, "name"是要删除的cookie的名称,
                                                   'optionsString'是该cookie的选项, 包括路径, 域
            5. delete_all_cookies(): 删除所有cookie信息
"""
import time

# 根据使用的浏览器, 导入对应模块
from selenium.webdriver import Chrome  # 谷歌浏览器对应模块
from selenium import webdriver

if __name__ == '__main__':
    # 浏览器安装非默认路径, 需指定浏览器安装路径
    options = webdriver.ChromeOptions()
    options.binary_location = r'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # 创建浏览器对象, 并传入初始化配置参数
    web = Chrome(options=options)
    # 打开百度
    web.get('http://www.baidu.com')
    # 设置浏览器窗口最大化
    web.maximize_window()
    # 指定关键字搜索内容, xpath定位搜索框, 输入要搜索内容的关键字
    web.find_element('xpath', '//*[@id="kw"]').send_keys(input('请输入搜索内容关键字:'))
    # xpath定位搜索按钮, 点击搜索
    web.find_element('xpath', '//*[@id="su"]').click()
    time.sleep(5)
    # 获取页面源码
    print(web.page_source)
    # 浏览器后退, 回到上个页面
    web.back()
    time.sleep(5)
    # 浏览器前进, 回到退回前的页面
    web.forward()
    time.sleep(2)
    # 刷新当前页面
    web.refresh()
    # 使页面显示5s后关闭
    time.sleep(5)
    # 关闭浏览器
    web.quit()
