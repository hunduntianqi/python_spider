"""
    xpath解析:
        最常用且最便捷高效的一种解析方式, 是一种通用性解析方式,
        除python外的其他编程语言也可使用xpath解析数据
        xpath解析原理:
            1. 实例化一个etree的对象, 将需要被解析的源码数据加载到该对象中
            2. 调用etree对象中的xpath方法, 结合xpath表达式实现标签的定位和内容的捕获
        环境安装:
            pip install lxml
        实例化etree对象:
            from lxml import etree
            1. 将本地的html文档中的源码数据加载到etree对象
                etree_object = etree.parse(filepath(页面源码文件路径))
            2. 将从互联网上获取到的源码数据加载到etree对象
                etree_object = etree.HTML('parse_text')
        xpath方法:
            etree_object.xpath('xpath表达式'), 返回定位到的标签节点对象列表
        xpath表达式:
            只能根据层级关系实现标签定位
            例:etree_object.xpath('/html/body/div/span/img/a'), 返回根据层级定位到的a节点对象列表
            '/':表示从根节点开始定位, 1个'/'表示一个层级
            '//': 表示多个层级, 例:etree_object.xpath('/html/body/div/span//a')， 返回根据层级定位到的
                  span标签下的a标签列表, 无论是否为span标签下的直接嵌套标签
            属性定位:tag[@属性名='属性值']
                例:etree_object.xpath('/html/body/div/span/img/a[@属性名称=属性值]')
                   etree_object.xpath('/html/body/div/span/img/a[@class='nextPage']')
                   定位class值为'nextPage'的a标签
            索引定位:tag[index]
                例:etree_object.xpath('/html/body/div/span/img/a[index]'), 返回索引值为index的a标签
                注:html中的索引值是从1开始的
            取文本和属性值:
                取文本:
                    1. tag/text(), 取得某标签中存储的直接文本内容
                    2. tag//text(), 可以取得标签中存储的所有文本内容, 包括嵌套标签内的文本内容
                取属性值:
                    tag/@属性名
"""