"""
    bs4解析原理:
            1. 实例化一个BeautifulSoup对象, 并且将页面源码加载到该对象中
            2. 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    解析步骤:
        1. 实例化BeautifulSoup对象
            from bs4 import BeautifulSoup
            1.1 将本地的html文档中的数据加载到该对象:
                fp = open('./本地html文件', 'r', encoding='utf-8')
                soup = BeautifulSoup(fp, 'lxml')
            1.2 将互联网上获取到的页面源码加载到该对象中:
                response = requests.get(url)
                soup = Beautiful(response.text, 'lxml')
        2. 调用Beautiful对象提供的方法和属性:
            2.1 soup.tagName: 获取第一个对应标签的全部内容
            2.2 soup.find('tagName'): 类似于soup.tagName
                soup.find(class_='类名'): 返回第一个对应类名的标签
                soup.find('tagName', class_='类名'): 返回对应标签中嵌套的满足类名的第一个标签
                注意: class定位属于属性定位, class也可以换做id等其他标签属性
            2.3 soup.find_all(): 与find()方法使用一致, 不过是返回所有满足条件的标签, 以列表形式
            2.4 soup.select('某种选择器'): 表示使用选择器定位标签, 包括类选择器, id选择器, 标签选择器等
                返回的是满足所有条件的标签, 以列表形式
                层级选择器代码格式:
                    soup.select('层级1 > 层级二 > 层级三 > 层级4....'):
                        每个层级可以使用不同形式的选择器进行定位
                    soup.select('层级1 > 层级二  层级4....'):
                        每个层级可以使用不同形式的选择器进行定位
                    注意:
                        层级选择器中: '>' 表示一个层级, '空格'表示间隔多个层级
            2.5 获取标签之间的文本数据:tagName.text/string/get_text():
                text/get_text(): 可以获取一个标签下的全部文本内容(包括该标签嵌套标签中的文本内容)
                string: 只能获取该标签下的文本内容, 不能获取嵌套标签中的文本内容
            2.6 获取标签中的属性值 ==> soup.tagName['对应属性名']
"""
