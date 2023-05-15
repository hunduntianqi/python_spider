from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()

web.get('http://www.chaojiying.com/user/login/')

time.sleep(2)
# 获取到图片的内容,二进制字节形式
img = web.find_element_by_xpath('/2022-1-12-html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# print(img)
# web.close()
chaojiying = Chaojiying_Client('17320101759', '2251789949gpt', '919742')
dic = chaojiying.PostPic(img, 1902)
print(dic)
print(dic['pic_str'])
time.sleep(3)
# 向页面中填入用户名,密码,验证码
user = web.find_element_by_xpath('/2022-1-12-html/body/div[3]/div/div[3]/div[1]/form/p[1]/input')
user.send_keys('17320101759')
password = web.find_element_by_xpath('/2022-1-12-html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')
password.send_keys('2251789949gpt')
check = web.find_element_by_xpath('/2022-1-12-html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')
check.send_keys(dic['pic_str'])
time.sleep(5)
# 点击登录
login = web.find_element_by_xpath('/2022-1-12-html/body/div[3]/div/div[3]/div[1]/form/p[4]/input')
login.click()
