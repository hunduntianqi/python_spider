"""
    CSV模块:  Python标准库模块
        作用:
            将爬取到的数据存放到本地csv文件中
        使用流程:
            1. 打开csv文件
            2. 初始化写入对象
                writer = csv.writer(csv文件对象)
            3. 写入数据(参数为列表)
                writerrow():单行写入
                    with open(path, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerrow(列表数据)
                writerrows(): 多行写入
                    with open(path, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerrows(元素为元组的列表)
"""
import csv

# 单行写入数据
with open('./csvTest.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'sex'])

# 多行写入
with open('./csvTest.csv', mode='a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([('name', 'age', 'sex'),
                      ('郭鹏涛', '24', '男'),
                      ('陈欣妮', '24', '女')
                      ])
