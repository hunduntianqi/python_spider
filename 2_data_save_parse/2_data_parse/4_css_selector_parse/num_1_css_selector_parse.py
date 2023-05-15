"""
    CSS选择器:
        1. id选择器: #
        2. 标签选择器: 标签
        3. 类选择器: .
        4. 选择器分组: ,
        5. 后代选择器: 空格
        6. 子选择器: >
        7. 相邻选择器: +
        8. 属性选择器: [属性=值]
    pyquery:
        使用CSS选择器解析数据
        1. 加载html内容
            p = pyquery.Pyquery(html)  # p为pyquery对象
        2. 解析内容:
           p1 = p('css选择器)  # p1也为pyquery对象
        3. 获取属性:
            p1.attr('属性名')
        4. 获取文本:
            p1.text(): 只获取该选择器定位标签下的文本
            p1.html(): 获取该选择器定位标签下的标签和文本内容
        5. 根据CSS选择器获取多个标签解析属性值:
            it = p('css选择器').items()  # it为一个生成器 / 迭代器对象
            遍历迭代器
            for item in it:
                属性 = item.attr('属性名')
                文本 = item.text()
        6. css选择器中标签索引: 标签:nth-child(索引值)
"""
