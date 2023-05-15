"""
    Scrapy框架:
        是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架
        常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中
    Scrapy框架特点:
        1. 为了爬取网络数据, 提取数据的应用框架
        2. Scrapy使用Twisted异步网络库来处理网络通讯
        3. Scrapy框架可以高效(爬取效率和开发效率)完成数据爬取
    Scrapy框架组件:
        1. 引擎-Engine:框架核心, 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯、信号、数据传递等
        2. 爬虫文件-Spider: 负责数据解析提取, 负责处理所有Responses,从中分析提取数据, 获取Item字段需要的数据,
                      并将需要跟进的URL提交给引擎, 再次进入Scheduler(调度器)
        3. 调度器-Scheduler: 负责维护请求队列, 接受引擎发送过来的Request请求, 并按照一定的方式进行整理排列, 入队,
                      当引擎需要时, 交还给引擎
        4. 下载器-Downloader: 负责向网站发送请求获取响应, 并将其获取到的Responses交还给Scrapy Engine(引擎),
                      由引擎交给Spider来处理
        5. 项目管道-Pipeline: 负责处理爬虫文件解析的数据(数据持久化), 处理Spider中获取到的Item, 并进行进行
                      后期处理(详细分析, 过滤, 存储)
        中间件:
            1. 下载中间件-Downloader Middlewares:
                请求对象->引擎->下载器, 包装请求(随机代理等)
            2. 蜘蛛中间件-Spider Middlewares:
                响应对象->引擎->爬虫文件, 可修改响应对象属性
    Scrapy框架执行流程:
        1. 引擎向爬虫文件索要第一批要爬取的url, 交给调度器入队列
        2. 调度器处理请求后出队列, 通过下载器中间件交给下载器下载
        3. 下载器得到响应对象后, 通过蜘蛛中间件交给爬虫文件
        4. 爬虫文件对数据进行解析提取
        5. 解析提取后的数据交给管道文件入库处理, 数据存储等
        6. 需要继续跟进的url, 再次交给调度器入队列, 循环执行
    Scrapy操作命令:
        1. 创建Scrapy项目:
            在要创建项目的路径下:
                scrapy startproject 项目名
                例:D:\Users\Administrator\IdeaProjects\python_爬虫\2022_1_29_Scrapy框架\Scrapy框架练习>scrapy startproject Baidu
        2. 创建爬虫文件模板:
            在项目目录下:
                scrapy genspider 爬虫文件名 允许爬取域名
                例:D:\Users\Administrator\IdeaProjects\python_爬虫\2022_1_29_Scrapy框架\Scrapy框架练习\Baidu>scrapy genspider baidu baidu.com
        3. 执行爬虫:
            方法一:在项目目录路径下, 终端运行命令: scrapy crawl 爬虫名
            方法二:在项目基本目录下新建py文件, 编写代码:
                from scrapy import cmdline # 导入模块
                cmdline.execute(['scrapy','crawl','爬虫名']) #运行代码方式一
                cmdline.execute('scrapy crawl 爬虫名'.split()) #运行代码方式二
    Scrapy项目目录:
        1.scrapy.cfg: 项目的配置文件
        2.mySpider/: 项目的Python模块, 将会从这里引用代码
        3.mySpider/items.py: 项目的目标文件
        4.mySpider/pipelines.py: 项目的管道文件
        5.mySpider/settings.py: 项目的设置文件
        6.mySpider/spiders/: 存储爬虫代码目录
    Scrapy爬虫步骤:
        1.创建一个Scrapy项目 ==> scrapy startproject 项目名
        2.创建爬虫文件 ==> scrapy genspider 爬虫文件名 允许爬取域名
        2.定义提取的结构化数据(Item)
        3.编写爬取网站的 Spider 并提取出结构化数据(Item)
        4.编写 Item Pipelines 来存储提取到的Item(即结构化数据)
    Scrapy数据持久化:
        1. 在settings.py文件中开启管道文件
        2. 在管道文件中编写open_spider(self, spider)方法:
            该方法在爬虫程序启动时只执行一次, 与__init__(self)方法类似, 一般用于数据库的链接和文件对象创建
            该方法在数据不需要存储时可以不存在, 对程序运行无影响
        3. 在管道文件中编写process_item(self, item, spider)方法:
            对数据进行处理, 一般为写入数据库或写入对应文件对象, 该方法为处理数据必须函数, 管道类中必须有
        4. 在管道文件中编写close_spider(self, spider)方法:
            爬虫程序结束时, 只执行一次, 一般用于数据库的断开和文件对象的关闭, 不需要存储时可以不存在, 对程序运行无影响
        注意:
            在settings.py文件中, 定义的管道文件类名必须在管道文件中存在, 否则会报错！！！
    下载器中间件:
        注意: Request()方法中所有的参数都可以作为请求对象request的属性
              Request()方法参数:url, meta, callback, headers, cookies, dont_filter
                            meta属性作用:
                                1. 在不同解析函数中传递数据
                                2. 定义代理IP:
                                    request.meta['proxy'] = proxy(含有代理IP的变量, 例:http://127.0.0.1:8080, 不是字典)
                            callback属性:指定响应对象对应解析函数:
                                scrapy.Request(url=url, callback=self.解析函数)
                            dont_filter属性:
                                定义请求是否去重, 默认为False, 表示去重, True表示不去重
        当开启下载中间件后, 在程序开始运行后, 在调度器把url交给下载器下载时, 会先被下载器中间件拦截, 执行settings.py文件中
        配置的对应类中的方法, 执行完毕后, 对request对象进行包装, 再交给下载器进行下载！！！
        例: User-Agent池-大量User-Agent获取:
            1. 定义获取User-Agent的类, 并在settings.py文件中进行配置
            2. from fake_useragent import UserAgent包
            3. 编写process_request(self, request, spider)方法, 定义变量存储随机生成的User-Agent
             例:from fake_useragent import UserAgent
                class BaiDuRandomDownloaderMiddleware(object):
                        def process_request(self, request, spider):
                            agent = UserAgent().Random
                            request.headers['User-Agent'] = agent
        其他中间件书写方法与User-Agent相似, 皆为定义类, 编写方法, 并在settings.py文件中配置, 多个中间件
        执行时由settings.py中优先级决定执行顺序！！！
        常用中间件:
            1. 随机User-Agent
            2. 随机代理IP
            3. 随机cookies:
                除在下载器中间件中定义外, 还要将settings.py文件中的COKIES_ENABLED设置为True
                COKIES_ENABLED:
                    注释: 表示禁用cookies
                    False: 表示使用settings.py文件中DEFAULT_REQUEST_HEADERS中的Cookies
                    True: 表示使用爬虫文件中Request()方法中的Cookies参数, 或者中间件中Cookies
    Scrapy框架发送POST请求:
        GET请求: yield scrapy.Request(url=url, meta={}, callback=...)
        POST请求: yield scrapy.FormRequest(url=url, formdata={}, meta={}, callback=...)
            发送POST请求时, 必须重写start_requests(self)方法, 该方法默认发送get请求
            重写步骤:
                1. 删掉start_urls列表
                2. 重写star_requests(self)方法, yield scrapy.FormRequest()方法
"""