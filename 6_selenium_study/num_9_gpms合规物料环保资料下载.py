"""
    GPMS合规物料查询 ==> selenium
"""
import os
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

if __name__ == '__main__':
    # 创建一个 chromeOptions 对象
    options = ChromeOptions()
    # 配置启动参数
    # 窗口最大化
    options.add_argument('--start-maximized')
    # 禁用浏览器被自动化程序控制的提示
    options.add_argument('--disable-infobars')
    # 设置文件下载路径
    path: str = input("请输入保存文件的文件夹路径:")
    prefs = {
        'profile.default_content_settings.popups': 0,  # 放置下载文件弹窗
        'download.default_directory': path  # 设置文件保存路径
    }
    options.add_experimental_option('prefs', prefs)
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
    # 选择物料审核管理
    web.find_element(by=By.XPATH, value="/html/body/form/div[2]/div[1]/ul/li[3]/a").click()
    # 选择物料归档
    web.find_element(by=By.XPATH, value="/html/body/form/div[2]/div[1]/ul/li[4]/a").click()
    # 定位frame()表单
    frame = web.find_element(by=By.XPATH, value='//*[@id="main"]')
    # 定位对象转换为frame
    web.switch_to.frame(frame)
    # 打开文件, 读取ICT PN
    workBook = load_workbook('ICT PN.xlsx')
    # 获取活动工作表
    sheet_list = workBook.active
    # 读取数据
    ict_pn_list = sheet_list['A']
    print(ict_pn_list)
    # 遍历列表
    for ict_pn in ict_pn_list:
        # 清空输入框并输入物料编码
        web.find_element(by=By.XPATH, value='//*[@id="wlbm"]').clear()
        web.find_element(by=By.XPATH, value='//*[@id="wlbm"]').send_keys(ict_pn.value.strip())
        # 查询数据
        web.find_element(by=By.XPATH, value='/html/body/div[2]/div[14]/a[2]').click()
        # 选中数据
        web.find_element(by=By.XPATH, value='//*[@id="divResult"]/tr/td[1]/div').click()
        # 导出数据
        web.find_element(by=By.XPATH, value='/html/body/div[2]/div[14]/a[1]').click()
        while True:
            if os.path.exists('{}/files.zip'.format(path)):
                file = open('{}/files.zip'.format(path), 'rb')
                filedata = file.read()
                file.close()
                os.remove('{}/files.zip'.format(path))
                with open('{}/{}-供应商提供环保资料.zip'.format(path, ict_pn.value), 'wb') as write_file:
                    write_file.write(filedata)
                    print('{}-供应商提供环保资料 已下载完成'.format(ict_pn.value))
                break
            else:
                pass
    time.sleep(5)
    pass
