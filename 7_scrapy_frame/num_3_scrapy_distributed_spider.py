"""
    分布式爬虫:
        指多台爬虫服务器同时抓取一个爬虫项目, 数据不重复
    分布式爬虫环境:
        需要有两台或两台以上的电脑或服务器, 并且其中一台服务器需要对负责对url做统一管理(个人验证可以使用虚拟机)！！
    分布式爬虫原理:
        多台主机共享一个爬取队列
        实现方法:
            Scrapy本身不支持分布式, 需要重写Scrapy的调度器与Redis结合实现分布式爬虫！！
            具体实现-scrapy_redis模块已重写scrapy调度器
        scrapy_redis分布式实现流程:
            1. scrapy_redis建立一个redis队列(自动去重)
            2. 调度器把爬虫文件生成的请求发送给redis队列
            3. 调度器再从redis队列中取出请求, 其他爬虫服务器也可以从队列中取出请求
            4. 每一个爬虫的调度器都从队列中取出请求和存入请求, 实现多个爬虫, 多台机器同时爬取数据
    Redis优势:
        1. 基于内存, 速度快, 可快速存取请求
        2. redis集合具有数据类型无序去重的特点, 可以用来存储每个请求的指纹
    scrapy_redis详解:
        settings.py:配置说明:
            1. 重新指定调度器:启用Redis调度存储请求队列:
                SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
            2. 重新指定去重机制, 确保所有的爬虫通过Redis去重:
                DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
            3. 是否清除请求指纹, 此变量允许爬虫暂停/恢复/断点续爬(默认False为清除, 设置为True为不清除):
                SCHEDULER_PERSIST = True
            4. 优先级队列:
                默认:
                    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
                先进先出:
                    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
                后进先出:
                    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
            5. Redis管道:
                此变量使数据可以存入Redis数据库
                ITEM_PIPELINES = {'scrapy_redis.pipelines.RedisPipeLine': 300}
            6. 指定连接到redis时使用的端口和地址:
                REDIS_HOST = 'IP地址'
                REDIS_PORT = 6379
                如果redis数据库设置有密码:
                    REDIS_URL = 'redis://user:pass@hostname:PORT'
    利用scrapy_redis实现分布式爬虫:
        scrapy本身不支持分布式, 需要先写非分布式爬虫, 然后通过以下方法实现分布式
        方法一: 配置settings.py实现
            1. 指定使用scrapy_redis的调度器:
                SCHEDULER = "scrapy_redis.scheduler.Scheduler"
            2. 指定使用scrapy_redis的去重机制:
                DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
            3. 指定redis的IP地址和端口号:
                REDIS_HOST = "reids数据库服务器IP地址"
                REDIS_PORT= 6379
            4. 添加scrapy_redis管道 - 把数据真正存入redis数据库(非必须)
                ITEM_PIPELINES = {
                    "scrapy_redis.pipelines.RedisPipeline":300
                }
            5. 将修改后的代码原封不动复制到所有要爬取数据的服务器
                然后启动程序

            6. 是否清除指纹:
                SCHEDULER_PERSIST = True(默认为False, 爬取完毕后清除指纹, 设置为True为不清除指纹)
        方法二: 使用redis_key实现(了解):
            1. 先按照方法一配置settings.py文件
            2. 爬虫文件中继承scrapy_redis的RedisSpider类, 并设置redis_key
                from scrapy_redis.spider import RedisSpider
                class 爬虫类(RedisSpider):
                    去掉start_urls, 设置redis_key
                    redis_key = "爬虫名:spider"
            3. 把代码复制到所有爬虫服务器, 并启动项目
            4. 到redis命令行, 执行LPUSH命令压入第一个要爬取的url地址
                LPUSH 爬虫名:spider 一级页面第一页的url地址
"""
