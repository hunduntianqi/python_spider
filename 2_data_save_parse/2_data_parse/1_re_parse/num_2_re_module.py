"""
    re模块 ==> python中用于操作解析正则表达式的模块
    re模块常用方法:
        1. re.findall(regex, str, re.S): 匹配字符串中所有符合正则的内容, 返回一个列表
        2. re.finditer(regex, str, re.S): 匹配字符串中所有的内容, 返回一个迭代器, 从迭
                                          代器中拿到内容需要.group()
        3. re.search(regex, str, re.S): 匹配字符串中符合条件的内容, 返回match对象, 拿到内容需要.group(), 匹配到
                        一个符合正则的内容就结束
        4. re.match(regex, str, re.S): 从字符串头部开始匹配, 第一个字符不符合正则会报错
        5. re.compile(regex): 用于预加载正则表达式, 返回一个包含正则匹配条件的对象, 该对象可直接调用
                              re模块用于解析正则的方法, 不需要在传入正则表达式, 例:
                              re_object = re.compile(r'\d+')
                              data_list = re_object.findall(str, re.S)
        说明: re.S 可以使得忽略换行等空白字符匹配数据
    re模块使用流程:
        方法一:
            r_list = re.findall('正则表达式', str, re.S)
            该方法返回结果为列表
        方法二:
            pattern = re.compile('正则表达式', re.S)
            r_list = pattern.findall(html)
        注意:
            1. findall()方法的到的结果一定为列表
            2. re.S作用为使正则表达式元字符.可匹配\n在内的所有字符
        匹配任意一个字符正则表达式:
            方法一:
                pattern = re.compile('[/s/S]')
                result = pattern.findall(str)
            方法二:
                pattern = re.compile('.*', re.S)
                result = pattern.findall(str)
    正则表达式分组匹配:
        匹配时先按照整体正则匹配, 然后再提取分组()中的内容
        如果有2个及以上分组(), 在结果中以元组形式显示[(), (), ()...]
"""

import re

r_list = re.findall('AB', 'ABCABCDEFGANC', re.S)
print(r_list)

# 分组示例
html = 'A B C D'
pattern = re.compile('\w+\s+\w+')
r_list = pattern.findall(html)
print(r_list)  # r_list = ['A B','C D']

pattern = re.compile('(\w+)\s+\w+')
r_list = pattern.findall(html)
print(r_list)  # r)list = ['A', 'C']

pattern = re.compile('(\w+)\s+(\w+)')
r_list = pattern.findall(html)
print(r_list)  # r_list = [('A', 'B'), ('C', 'D')]
