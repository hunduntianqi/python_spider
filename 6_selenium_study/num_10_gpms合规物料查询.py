"""
    GPMS合规物料查询 ==> selenium
"""
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    # 创建一个 chromeOptions 对象
    options = ChromeOptions()
    # 配置启动参数
    # 窗口最大化
    options.add_argument('--start-maximized')
    # 禁用浏览器被自动化程序控制的提示
    options.add_argument('--disable-infobars')
    # 创建谷歌浏览器对象
    web = Chrome(options=options)
    # 打开目标浏览器
    web.get("xxxx")
    # 定位'企业内部用户'
    web.find_element(by=By.XPATH, value="/html/body/form/div[2]/div[1]/div/div[1]/a[2]").click()
    # 输入用户名和密码
    web.find_element(by=By.XPATH, value='//*[@id="OrganizeLoginName"]').send_keys("HA49412")
    web.find_element(by=By.XPATH, value='//*[@id="OrganizePassWord"]').send_keys("Rqh1234567890-=.")
    # 点击登录
    web.find_element(by=By.XPATH, value='//*[@id="OrganizeLogin"]').click()
    # 选择报表管理
    web.find_element(by=By.XPATH, value="/html/body/form/div[2]/div[1]/ul/li[7]/a").click()
    # 选择供应商反馈情况统计
    web.find_element(by = By.XPATH, value="/html/body/form/div[2]/div[1]/ul/li[8]/a[1]").click()
    # 定位frame()表单
    frame = web.find_element(by=By.XPATH, value='//*[@id="main"]')
    # 定位对象转换为frame
    web.switch_to.frame(frame)
    # 定位获取select对象
    select_wlzt = Select(web.find_element(by=By.XPATH, value='//*[@id="wlzt"]'))
    # 选中物料合规元素
    select_wlzt.select_by_value("State|2")
    # 点击查询
    web.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[7]/a[2]').click()
    # 点击导出
    web.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[7]/a[1]').click()
    time.sleep(5)
    pass
