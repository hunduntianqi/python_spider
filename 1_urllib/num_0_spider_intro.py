"""
    什么是爬虫(spider):
        写程序,然后去互联网上抓取数据的过程
    互联网: 有很多标签a连接组成, 网得节点就是每一个 a 标签链接
    url：统一资源定位符
    可以实现爬虫的语言:
        1.python:语法简单,代码优美,学习成本低支持第三方模块多,拥有一个非常强大的scrapy框架
        2.php:多进程,多线程支持不好
        3.java:爬虫方面较为优秀,在爬虫方面是python的最主要竞争对手,缺点是代码教多,修改不方便
                重构成本大！！！
        4.c,c++:几乎没有人用来做爬虫,是能力的体现,但不是很好的选择
    通用爬虫: 百度,360,搜狐,谷歌等搜索引擎
        原理:
            1.抓取网页
            2.采集数据
            3.数据处理
            4.提供检索服务
        通用爬虫如何抓取新网站:
            1.主动提交url
            2.设置友情链接
            3.搜索引擎和DNS服务商合作抓取新网站
        检索排名:
            1. 竞价排名(花钱)
            2. 根据pagerank值(访问量、点击量)来排名
        robots.txt: 爬虫协议, 规定哪些爬虫程序可以爬取该网站数据, 以及可以爬取哪些数据
    聚焦爬虫:
        根据特定的需求,抓取指定的数据,代替浏览器上网
        网页的特点:
            (1) 网页都有自己唯一的url
            (2) 网页内容都是HTML的结构
            (3) 使用的都是http,https协议
        爬取步骤:
            (1) 给一个url
            (2) 写程序, 模拟浏览器访问url
            (3) 解析内容, 提取数据
    善意的爬虫: 不破坏被抓取网站的资源, 正常访问,不窃取用户隐私
    恶意的爬虫: 影响网站的正常运营(抢票, 秒杀, 疯狂solo网站资源造成网络宕机)
    反爬机制: 门户网站可以通过指定相应的策略或者技术手段, 防止爬虫程序进行网站数据的爬取
    反反爬策略: 爬虫程序可以通过制定相关的策略或者技术手段, 破解门户网站中具备的反爬机制,
               从而获取门户网站中相关的数据
"""
