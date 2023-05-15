import time

import requests
from fake_useragent import UserAgent
import re
import os

try:
    os.mkdir('./vmgirs')
except:
    print('文件夹已存在！！')

headers = {
    'user-agent': str(UserAgent().random),
    'Referer': 'https://www.vmgirls.com/',
    'Cookie': 'Hm_lvt_a5eba7a40c339f057e1c5b5ac4ab4cc9=1646447887; _gid=GA1.2.579827981.1646447888; __cf_bm=9UOVKVmFVX4ZmCOcX05kL1C4zuCwTSy6w.VgNAC9PMs-1646447905-0-ARuWXPjH1CMRIxn6Vm2T3ita/LmKHxPburk84At2wb2OOEEGj2pmZraoU+ZwU1SnAbWskgVwsrhYclkNIJF6c0j1WbHpDx6wF61g0UGTmLlqjrggguqHhk2/mRSilc98EQ==; PHPSESSID=3sh2t1ggnltdni791rg7o0df0i; _gat_gtag_UA_127463675_2=1; _ga_2VEZ2J9RNH=GS1.1.1646447887.1.1.1646448266.56; _ga=GA1.2.1763310964.1646447887; Hm_lpvt_a5eba7a40c339f057e1c5b5ac4ab4cc9=1646448267'
}

start_url = 'https://www.vmgirls.com'
response = requests.get(start_url, headers=headers)
# print(response.text)
regex = 'li id=".*?" class="menu-item menu-item-type.*?"><a target="_blank" rel="noopener" href="(.*?)">(.*?)</a></li>'
pattern = re.compile(regex, re.S)
type_list = pattern.findall(response.text)
print(type_list)

for i in type_list[10:19]:
    print(i, type_list.index(i))
    try:
        os.mkdir('./vmgirs/{}'.format(i[1].split('<')[0]))
    except:
        print('文件夹已存在！！')
    regex_2 = '<a class="media-content" target="_blank" href="(.*?)" title="(.*?)"'
    response_2 = requests.get(i[0], headers=headers)
    list_2 = re.compile(regex_2, re.S).findall(response_2.text)
    # print(list_2)
    for type_pic in list_2:
        try:
            os.mkdir('./vmgirs/{}/{}'.format(i[1].split('<')[0], type_pic[1]))
        except:
            print('文件夹已存在！！')
        print(type_pic)
        regex_3 = '<a href="(.*?)" alt="{}"'.format(type_pic[1])
        response_3 = requests.get(type_pic[0], headers=headers)
        list_3 = re.compile(regex_3).findall(response_3.text)
        print(list_3)
        for pic_lic in list_3:
            pic_name = pic_lic.split('/')[-1]
            pic_link = 'https:' + pic_lic
            res_pic = requests.get(pic_link, headers=headers)
            with open('./vmgirs/{}/{}/{}'.format(i[1].split('<')[0], type_pic[1], pic_name), 'wb') as file:
                file.write(res_pic.content)
        time.sleep(1)
